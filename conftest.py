import pytest

tests_to_xfail = [
    # scipy/_lib/tests
    "test__threadsafety.py::test_parallel_threads",
    "test__util.py::test_pool",
    "test__util.py::test_mapwrapper_parallel",
    "test_ccallback.py::test_threadsafety",
    "test_import_cycles.py::test_modules_importable",
    # scipy/fft/tests
    "test_fft_function.py::test_fft_function",
    "test_multithreading.py::test_threaded_same",
    "test_multithreading.py::test_mixed_threads_processes",
    "test_numpy.py::TestFFTThreadSafe",
    "test_numpy.py::test_multiprocess",
    # scipy/ndimage/tests
    "test_filters.py::TestThreading",
    # scipy/signal/tests
    "test_signaltools.py::TestMedFilt.test_medfilt2d_parallel",
    # scipy/sparse/linalg/_dsolve/tests
    "test_linsolve.py::TestSplu.test_threads_parallel",
    # scipy/sparse/linalg/_eigen/arpack/tests
    "test_arpack.py::test_parallel_threads",
    # scipy/spatial/tests
    "test_kdtree.py::test_query_ball_point_multithreading",
    "test_kdtree.py::test_ckdtree_parallel",
    # scipy/sparse/tests
    "test_sparsetools.py::test_threads",
]

def pytest_collection_modifyitems(config, items):
    marker = pytest.mark.xfail(reason=("Known Pyodide limitation"))
    for item in items:
        path, line, name = item.reportinfo()
        path = str(path)
        full_name = f"{path}::{name}"
        if any(each in full_name for each in tests_to_xfail):
            print(full_name)
            item.add_marker(marker)
