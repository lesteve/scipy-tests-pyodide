import re

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

# Those tests need to be skipped because they crash Pyodide, typically
# signature mismatch or memory corruption
tests_to_skip = [
    # scipy/linalg tests
    # memory corruption
    "test_basic.py.+test_hermitian",
    # memory corruption
    "test_basic.py.+TestLstsq.+random_exact",
    # signature mismatch
    "test_blas.+test_complex_dotu",
    # signature mismatch
    "test_cython_blas.+complex",
    # missing symbol
    "test_decomp_cossin",
    # signature mismatch
    "test_lapack.py.+larfg_larf",
    # missing symbols
    "test_lapack.py.+geqrt_gemqrt",
    "test_lapack.py.+tpqrt_tpmqrt",
    "test_lapack.py.+test_geqrfp",
    "test_lapack.py.+orcsd_uncsd",
    "test_lapack.py.+test_gtsvx_error_singular",
    # scipy/optimize/tests
    # memory corruption
    "test_minpack.py.+test_reentrant_func",
    # scipy/sparse/tests
    # signature mismatch
    "test_propack",
    # memory corruption
    "test_gcrotmk.+test_cornercase",
    "test_iterative.+precond_dummy",
    "test_iterative.+test_convergence",
    "test_iterative.+gcrotmk",
    "test_iterative.+lgmres",
    "test_iterative.+test_maxiter$",
    # scipy/stats/tests
    # seems like a memory corruption (not deterministic not always the same
    # parametetrized tests that fails)
    "test_resampling.+TestMonteCarloHypothesisTest.+test_against_anderson.+logistic",
]

def pytest_collection_modifyitems(config, items):
    xfail_marker = pytest.mark.xfail(reason=("Known Pyodide limitation"))
    skip_marker = pytest.mark.skip(reason=("Avoid crashing Pyodide"))
    for item in items:
        path, line, name = item.reportinfo()
        path = str(path)
        full_name = f"{path}::{name}"
        if any(re.search(each, full_name) for each in tests_to_xfail):
            item.add_marker(xfail_marker)

        if any(re.search(each, full_name) for each in tests_to_skip):
            item.add_marker(skip_marker)
