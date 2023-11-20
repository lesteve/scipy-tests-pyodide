import re
import pytest

xfail = pytest.mark.xfail
skip = pytest.mark.skip

fp_exception_msg = (
    "no floating point exceptions, "
    "see https://github.com/numpy/numpy/pull/21895#issuecomment-1311525881"
)
process_msg = "no process support"
thread_msg = "no thread support"
signature_mismatch_msg = "signature mismatch"
memory_corruption_msg = "memory corruption"
temporary_jspi_msg = (
    "JSPI temporary skipping, see https://github.com/pyodide/pyodide/issues/4249"
)
temporary_meson_msg = (
    "temporary skipping after switch to meson, see https://github.com/pyodide/pyodide/issues/4310"
)

tests_to_mark = [
    # scipy/_lib/tests
    (
        "test__threadsafety.py::test_parallel_threads",
        xfail,
        thread_msg,
    ),
    ("test__threadsafety.py::test_parallel_threads", xfail, thread_msg),
    ("test__util.py::test_pool", xfail, process_msg),
    ("test__util.py::test_mapwrapper_parallel", xfail, process_msg),
    ("test_ccallback.py::test_threadsafety", xfail, thread_msg),
    ("test_import_cycles.py::test_modules_importable", xfail, process_msg),
    ("test_import_cycles.py::test_public_modules_importable", xfail, process_msg),
    # scipy/fft/tests
    ("test_fft_function.py::test_fft_function", xfail, process_msg),
    ("test_multithreading.py::test_threaded_same", xfail, thread_msg),
    (
        "test_multithreading.py::test_mixed_threads_processes",
        xfail,
        thread_msg,
    ),
    ("test_multithreading.py::test_threaded_same", skip, temporary_jspi_msg),
    (
        "test_multithreading.py::test_mixed_threads_processes",
        skip,
        temporary_jspi_msg,
    ),
    ("test_numpy.py::TestFFTThreadSafe", xfail, thread_msg),
    ("test_numpy.py::test_multiprocess", xfail, process_msg),
    # scipy/integrate tests
    ("test__quad_vec.py::test_quad_vec_pool", xfail, process_msg),
    ("test_quadpack.py.+test_variable_limits", skip, memory_corruption_msg),
    (
        "test_quadpack.py.+test_fixed_limits",
        skip,
        "test does not complete in 20 minutes",
    ),
    (
        "test_quadpack.py.+triple_integral_improper",
        skip,
        "parametrized tests that all fail and take ~9 minutes overall",
    ),
    # scipy/linalg/_dsolve tests
    ("test_linsolve.py::TestSplu.+(spilu_nnz0|splu_basic)", skip, temporary_jspi_msg),
    # scipy/linalg tests
    ("test_blas.+test_complex_dotu", skip, signature_mismatch_msg),
    ("test_cython_blas.+complex", skip, signature_mismatch_msg),
    ("test_lapack.py.+larfg_larf", skip, signature_mismatch_msg),
    # scipy/ndimage/tests
    ("test_filters.py::TestThreading", xfail, thread_msg),
    # scipy/optimize/tests
    (
        "test__differential_evolution.py::"
        "TestDifferentialEvolutionSolver.test_immediate_updating",
        xfail,
        process_msg,
    ),
    (
        "test__differential_evolution.py::TestDifferentialEvolutionSolver.test_parallel",
        xfail,
        process_msg,
    ),
    ("test_minpack.py.+test_reentrant_func", skip, memory_corruption_msg),
    ("test_minpack.py::TestFSolve.test_concurrent.+", xfail, process_msg),
    ("test_minpack.py::TestLeastSq.test_concurrent+", xfail, process_msg),
    ("test_optimize.py::test_cobyla_threadsafe", xfail, thread_msg),
    ("test_optimize.py::TestBrute.test_workers", xfail, process_msg),
    ("test_zeros.py::.+(gh3089_8394|gh18171)", skip, temporary_jspi_msg),
    # scipy/signal/tests
    (
        "test_signaltools.py::TestMedFilt.test_medfilt2d_parallel",
        xfail,
        thread_msg,
    ),
    # scipy/sparse/tests
    ("test_arpack.py::test_parallel_threads", xfail, thread_msg),
    ("test_linsolve.py::TestSplu.test_threads_parallel", xfail, thread_msg),
    ("test_propack", skip, signature_mismatch_msg),
    ("test_sparsetools.py::test_threads", xfail, thread_msg),
    ("test_array_api.py::test_sparse_dense_divide", xfail, fp_exception_msg),
    ("test_matfuncs.py::TestExpM.test_logm_consistency", skip, temporary_meson_msg),
    # scipy/spatial/tests
    (
        "test_kdtree.py::test_query_ball_point_multithreading",
        xfail,
        thread_msg,
    ),
    ("test_kdtree.py::test_ckdtree_parallel", xfail, thread_msg),
    # scipy/special/tests
    ("test_cython_special.py::test_cython_api.+erfinv", skip, temporary_jspi_msg),
    (
        "test_erfinv.py::TestInverseErrorFunction.test_domain_bounds.+erfinv.+(below|above)",
        skip,
        temporary_jspi_msg,
    ),
    (
        "test_nan_inputs.py::test_nan_inputs.+powm1",
        skip,
        temporary_jspi_msg,
    ),
    (
        "test_powm1.py::test_powm1.+(nan|inf)",
        skip,
        temporary_jspi_msg,
    ),
    # scipy/stats/tests
    ("test_qmc.py::TestVDC.test_van_der_corput", xfail, thread_msg),
    ("test_qmc.py::TestHalton.test_workers", xfail, thread_msg),
    ("test_qmc.py::TestUtils.test_discrepancy_parallel", xfail, thread_msg),
    (
        "test_resampling.+TestMonteCarloHypothesisTest.+test_against_anderson.+logistic",
        skip,
        memory_corruption_msg,
    ),
    ("test_sampling.py::test_threading_behaviour", xfail, thread_msg),
    ("test_stats.py::TestMGCStat.test_workers", xfail, process_msg),
    (
        "test_stats.py::TestKSTwoSamples.testLargeBoth",
        skip,
        "test taking > 5 minutes after scipy 1.10.1 update",
    ),
    (
        "test_multivariate.py::TestMultivariateT.test_cdf_against_generic_integrators",
        skip,
        "tplquad integration does not seem to converge",
    ),
    (
        "test_continuous_basic.py::.+studentized_range-args96-isf",
        skip,
        temporary_jspi_msg,
    ),
    (
        "test_distributions.py::TestStudentizedRange.+test_ppf_against_tables",
        skip,
        temporary_jspi_msg,
    ),
    (
        "test_hypotests.py::TestTukeyHSD",
        skip,
        temporary_jspi_msg,
    ),
    (
        "test_qmc.py::TestUtils.+test_discrepancy_parallel",
        skip,
        temporary_jspi_msg,
    ),
    (
        "test_qmc.py::TestVDC.+test_van_der_corput",
        skip,
        temporary_jspi_msg,
    ),
    (
        "test_qmc.py::TestHalton.+test_workers",
        skip,
        temporary_jspi_msg,
    ),
    (
        "test_qmc.py::TestVDC.+test_van_der_corput",
        skip,
        temporary_jspi_msg,
    ),

]


def pytest_collection_modifyitems(config, items):
    for item in items:
        path, line, name = item.reportinfo()
        path = str(path)
        full_name = f"{path}::{name}"
        for pattern, mark, reason in tests_to_mark:
            if re.search(pattern, full_name):
                # print(full_name)
                item.add_marker(mark(reason=reason))
