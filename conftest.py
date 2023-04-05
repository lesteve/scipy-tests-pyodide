import re
import pytest

xfail = pytest.mark.xfail
skip = pytest.mark.skip

tests_to_mark = [
    # scipy/_lib/tests
    (
        "test__threadsafety.py::test_parallel_threads",
        xfail,
        "no threading support",
    ),
    ("test__threadsafety.py::test_parallel_threads", xfail, "no threading support"),
    ("test__util.py::test_pool", xfail, "no process support"),
    ("test__util.py::test_mapwrapper_parallel", xfail, "no process support"),
    ("test_ccallback.py::test_threadsafety", xfail, "no threading support"),
    ("test_import_cycles.py::test_modules_importable", xfail, "no process support"),
    # scipy/fft/tests
    ("test_fft_function.py::test_fft_function", xfail, "no process support"),
    ("test_multithreading.py::test_threaded_same", xfail, "no threading support"),
    (
        "test_multithreading.py::test_mixed_threads_processes",
        xfail,
        "no threading support",
    ),
    ("test_numpy.py::TestFFTThreadSafe", xfail, "no threading support"),
    ("test_numpy.py::test_multiprocess", xfail, "no process support"),
    # scipy/linalg tests
    ("test_basic.py.+test_hermitian", skip, "memory corruption"),
    ("test_basic.py.+TestLstsq.+random_exact", skip, "memory corruption"),
    ("test_blas.+test_complex_dotu", skip, "signature mismatch"),
    ("test_cython_blas.+complex", skip, "signature mismatch"),
    ("test_decomp_cossin", skip, "missing symbol"),
    ("test_lapack.py.+larfg_larf", skip, "missing symbol"),
    ("test_lapack.py.+geqrt_gemqrt", skip, "missing symbol"),
    ("test_lapack.py.+tpqrt_tpmqrt", skip, "missing symbol"),
    ("test_lapack.py.+test_geqrfp", skip, "missing symbol"),
    ("test_lapack.py.+orcsd_uncsd", skip, "missing symbol"),
    ("test_lapack.py.+test_gtsvx_error_singular", skip, "missing symbol"),
    # scipy/ndimage/tests
    ("test_filters.py::TestThreading", xfail, "no threading support"),
    # scipy/optimize/tests
    ("test_minpack.py.+test_reentrant_func", skip, "memory corruption"),
    ("test_optimize.py::test_cobyla_threadsafe", xfail, "no threading support"),
    (
        "TestDifferentialEvolutionSolver.test_immediate_updating",
        xfail,
        "no process support",
    ),
    ("TestDifferentialEvolutionSolver.test_parallel", xfail, "no process support"),
    ("TestFSolve.test_concurrent.+", xfail, "no process support"),
    ("TestBrute.test_workers", xfail, "no process support"),
    # scipy/signal/tests
    (
        "test_signaltools.py::TestMedFilt.test_medfilt2d_parallel",
        xfail,
        "no threading support",
    ),
    # scipy/sparse/tests
    ("test_linsolve.py::TestSplu.test_threads_parallel", xfail, "no threading support"),
    ("test_arpack.py::test_parallel_threads", xfail, "no threading support"),
    ("test_propack", skip, "signature mismatch"),
    ("test_gcrotmk.+test_cornercase", skip, "memory corruption"),
    ("test_iterative.+precond_dummy", skip, "memory corruption"),
    ("test_iterative.+test_convergence", skip, "memory corruption"),
    ("test_iterative.+gcrotmk", skip, "memory corruption"),
    ("test_iterative.+lgmres", skip, "memory corruption"),
    ("test_iterative.+test_maxiter$", skip, "memory corruption"),
    ("test_sparsetools.py::test_threads", xfail, "no threading support"),
    # scipy/spatial/tests
    (
        "test_kdtree.py::test_query_ball_point_multithreading",
        xfail,
        "no threading support",
    ),
    ("test_kdtree.py::test_ckdtree_parallel", xfail, "no threading support"),
    # scipy/stats/tests
    (
        "test_resampling.+TestMonteCarloHypothesisTest.+test_against_anderson.+logistic",
        skip,
        "memory corruption",
    ),
    ("test_sampling.py::test_threading_behaviour", xfail, "no threading support"),
    ("test_stats.py::TestMGCStat::test_workers", xfail, "no process support"),
]


def pytest_collection_modifyitems(config, items):
    for item in items:
        path, line, name = item.reportinfo()
        path = str(path)
        full_name = f"{path}::{name}"
        for pattern, mark, reason in tests_to_mark:
            if re.search(pattern, full_name):
                item.add_marker(mark(reason=reason))
