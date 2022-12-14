import shlex
import sys
import itertools
import unittest
import asyncio


# This is the output of the command run from the scipy root folder:
# find scipy -name tests | sort | perl -pe 's@/@.@g'
test_submodules_str = """
scipy._build_utils.tests
scipy.cluster.tests
scipy.constants.tests
scipy.fftpack.tests
scipy.fft._pocketfft.tests
scipy.fft.tests
scipy.integrate._ivp.tests
scipy.integrate.tests
scipy.interpolate.tests
scipy.io.arff.tests
scipy.io._harwell_boeing.tests
scipy.io.matlab.tests
scipy.io.tests
scipy._lib.tests
scipy.linalg.tests
scipy.misc.tests
scipy.ndimage.tests
scipy.odr.tests
scipy.optimize.tests
scipy.optimize._trustregion_constr.tests
scipy.signal.tests
scipy.sparse.csgraph.tests
scipy.sparse.linalg._dsolve.tests
scipy.sparse.linalg._eigen.arpack.tests
scipy.sparse.linalg._eigen.lobpcg.tests
scipy.sparse.linalg._eigen.tests
scipy.sparse.linalg._isolve.tests
scipy.sparse.linalg.tests
scipy.sparse.tests
scipy.spatial.tests
scipy.spatial.transform.tests
scipy.special.tests
scipy.stats.tests
"""

test_submodules = test_submodules_str.split()

expected_test_results_by_category = {
    "failed": [
        "scipy.fft.tests",
        "scipy.interpolate.tests",
        "scipy._lib.tests",
        "scipy.ndimage.tests",
        "scipy.signal.tests",
        "scipy.sparse.linalg._dsolve.tests",
        "scipy.sparse.linalg._eigen.arpack.tests",
        "scipy.sparse.tests",
        "scipy.spatial.tests",
        "scipy.special.tests",
    ],
    "fatal error or timeout": [
        "scipy.linalg.tests",
        "scipy.optimize.tests",
        "scipy.sparse.linalg._isolve.tests",
        "scipy.sparse.linalg.tests",
        "scipy.stats.tests",
    ],
    "passed": [
        "scipy._build_utils.tests",
        "scipy.cluster.tests",
        "scipy.constants.tests",
        "scipy.fftpack.tests",
        "scipy.fft._pocketfft.tests",
        "scipy.io.arff.tests",
        "scipy.io._harwell_boeing.tests",
        "scipy.io.matlab.tests",
        "scipy.misc.tests",
        "scipy.odr.tests",
        "scipy.optimize._trustregion_constr.tests",
        "scipy.sparse.csgraph.tests",
        "scipy.sparse.linalg._eigen.lobpcg.tests",
        "scipy.sparse.linalg._eigen.tests",
        "scipy.spatial.transform.tests",
    ],
    "pytest usage error": [
        "scipy.integrate._ivp.tests",
    ],
    "tests collection error": [
        "scipy.integrate.tests",
        "scipy.io.tests",
    ],
}


async def _read_stream(stream, cb, timeout_without_output):
    while True:
        loop = asyncio.get_event_loop_policy().get_event_loop()

        async def readline(stream):
            return await stream.readline()

        task = loop.create_task(readline(stream))

        line = await asyncio.wait_for(task, timeout_without_output)
        line = line.decode()
        if line:
            cb(line)
        else:
            break


async def _stream_subprocess(cmd, stdout_cb, stderr_cb, timeout_without_output):
    process = await asyncio.create_subprocess_exec(
        *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    loop = asyncio.get_event_loop_policy().get_event_loop()

    stdout_task = loop.create_task(
        _read_stream(
            process.stdout, stdout_cb, timeout_without_output=timeout_without_output
        )
    )
    stderr_task = loop.create_task(
        _read_stream(
            process.stderr, stderr_cb, timeout_without_output=timeout_without_output
        )
    )

    stdout_result, stderr_result = await asyncio.gather(
        stdout_task, stderr_task, return_exceptions=True
    )

    if isinstance(stdout_result, asyncio.exceptions.TimeoutError) and isinstance(
        stderr_result, asyncio.exceptions.TimeoutError
    ):
        process.kill()
        # return None for timeout
        return

    return await process.wait()


def execute_command_with_timeout(command_list, timeout_without_output):
    """Run command while showing its stdout and stderr continuously.

    Returns
    -------
    dict containing exit_code, stdout, stderr
    """
    loop = asyncio.get_event_loop_policy().get_event_loop()

    stdout_list = []
    stderr_list = []

    def stdout_cb(line):
        print(line, end="")
        stdout_list.append(line)

    def stderr_cb(line):
        sys.stderr.write(line)
        stderr_list.append(line)

    rc = loop.run_until_complete(
        _stream_subprocess(command_list, stdout_cb, stderr_cb, timeout_without_output)
    )
    stdout = "\n".join(stdout_list)
    stderr = "\n".join(stderr_list)
    return {"exit_code": rc, "stdout": stdout, "stderr": stderr}


def run_tests_for_module(module_str):
    # some tests in scipy.interpolate e.g.
    # test_rbfinterp.py::TestRBFInterpolatorNeighborsInf::test_chunking can
    # take more than 60s to run
    timeout_without_output = 120 if 'interpolate' in module_str else 60
    command_str = f"node --experimental-fetch scipy-pytest.js -v {module_str}"
    command_list = shlex.split(command_str)
    command_result = execute_command_with_timeout(
        command_list=command_list, timeout_without_output=timeout_without_output
    )

    if command_result["exit_code"] is None:
        print(f"{module_str} timed out", flush=True)
    else:
        print(
            f"{module_str} exited with exit code {command_result['exit_code']}",
            flush=True,
        )

    return command_result


def exit_code_to_category(exit_code):
    if exit_code == 0:
        return "passed"
    if exit_code == 1:
        return "failed"
    if exit_code == 2:
        return "tests collection error"
    if exit_code == 4:
        return "pytest usage error"
    if exit_code == 5:
        return "no test collected"

    # this also covers exit code 3 which is pytest internal error, because this
    # is one of the symptom of a wasm memory corruption
    return "fatal error or timeout"


def print_summary(module_results):
    print()
    print("=" * 80)
    print("Test results summary")
    print("=" * 80)

    for each in module_results:
        print(f"{each['module']} {each['category']} (exit code {each['exit_code']})")

    print()
    print("-" * 80)
    print("Grouped by category:")
    print("-" * 80)

    def fun(each):
        return each["category"]

    test_results_by_category = {
        category: [each["module"] for each in group]
        for category, group in itertools.groupby(sorted(module_results, key=fun), fun)
    }
    for category, module_list in test_results_by_category.items():
        print(f"category {category} ({len(module_list)} modules)")
        for each in module_list:
            print(f"    {each}")

    sys.stdout.flush()

    # Compare test results with expectations. Easiest way I found to compare
    # dicts with a good error message is to use unittest
    tc = unittest.TestCase()
    # to show full info about the diff
    tc.maxDiff = None
    test_results_with_sets = {k: set(v) for k, v in test_results_by_category.items()}
    expected_test_results_with_sets = {
        k: set(v) for k, v in expected_test_results_by_category.items()
    }
    tc.assertDictEqual(expected_test_results_with_sets, test_results_with_sets)
    print("Test results matched expected ones")


def main():
    module_results = []

    custom_pytest_args = shlex.join(sys.argv[1:])
    if custom_pytest_args:
        global test_submodules
        test_submodules = [custom_pytest_args]

    for module in test_submodules:
        print("-" * 80, flush=True)
        print(module, flush=True)
        print("-" * 80, flush=True)
        this_module_result = run_tests_for_module(module)
        this_module_result["module"] = module
        this_module_result["category"] = exit_code_to_category(
            this_module_result["exit_code"]
        )
        module_results.append(this_module_result)

    # When using custom pytest args, we run a single pytest command and it does
    # not make sense to compare results to expectation
    if not custom_pytest_args:
        print_summary(module_results)


if __name__ == "__main__":
    main()
