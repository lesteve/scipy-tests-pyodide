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
todo_signature_mismatch_msg = "TODO signature mismatch"
todo_memory_corruption_msgt = "TODO memory corruption"
todo_genuine_difference_msg = "TODO genuine difference to be investigated"

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
    ("::TestFFTThreadSafe", xfail, thread_msg),
    ("::test_multiprocess", xfail, process_msg),
    # scipy/integrate tests
    ("test__quad_vec.py::test_quad_vec_pool", xfail, process_msg),
    ("test_quadpack.py.+test_variable_limits", skip, todo_memory_corruption_msgt),
    (
        "test_quadpack.py.+test_fixed_limits",
        skip,
        "TODO test does not complete in 20 minutes",
    ),
    (
        "test_quadpack.py.+triple_integral_improper",
        skip,
        "TODO parametrized tests that all fail and take ~9 minutes overall",
    ),
    (
        "test_quadpack.py.+TestMultivariateCtypesQuad.test_threadsafety",
        xfail,
        thread_msg,
    ),
    (
        "test_quadpack.py.+TestCtypesQuad.test_ctypes.*",
        xfail,
        "Test relying on finding libm.so shared library",
    ),
    (
        "test_quadpack.py.+TestQuad.test_double_integral.*",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_quadpack.py.+TestQuad.test_triple_integral",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_quadpack.py.+TestNQuad.test_square.*ranges_and_opts",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_quadrature.py.+TestQMCQuad.test_basic",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_quadrature.py.+TestQMCQuad.test_sign",
        xfail,
        todo_genuine_difference_msg,
    ),
    # scipy/interpolate
    (
        "test_fitpack.+test_kink",
        xfail,
        "TODO error not raised, maybe due to no floating point exception?",
    ),
    ("test_interpolate.+test_integrate_2d", xfail, todo_genuine_difference_msg),
    # scipy/linalg tests
    ("test_blas.+test_complex_dotu", skip, todo_signature_mismatch_msg),
    ("test_cython_blas.+complex", skip, todo_signature_mismatch_msg),
    ("test_lapack.py.+larfg_larf", skip, todo_signature_mismatch_msg),
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
    (
        "test__shgo.py.+test_19_parallelization",
        xfail,
        process_msg,
    ),
    (
        "test__shgo.py.+",
        xfail,
        "Test failing on 32bit (skipped on win32)",
    ),
    (
        "test_linprog.py::TestLinprogSimplexNoPresolve.test_bounds_infeasible_2",
        xfail,
        "TODO no warnings emitted maybe due to no floating point exception?",
    ),
    ("test_minpack.py.+test_reentrant_func", skip, todo_memory_corruption_msgt),
    ("test_minpack.py::TestFSolve.test_concurrent.+", xfail, process_msg),
    ("test_minpack.py::TestLeastSq.test_concurrent+", xfail, process_msg),
    (
        "test_minpack.py::TestFSolve.test_reentrant_Dfunc",
        xfail,
        todo_genuine_difference_msg,
    ),
    ("test_optimize.py::test_cobyla_threadsafe", xfail, thread_msg),
    ("test_optimize.py::TestBrute.test_workers", xfail, process_msg),
    # scipy/signal/tests
    (
        "test_signaltools.py::TestMedFilt.test_medfilt2d_parallel",
        xfail,
        thread_msg,
    ),
    # scipy/sparse/tests
    ("test_arpack.py::test_parallel_threads", xfail, thread_msg),
    ("test_array_api.py::test_sparse_dense_divide", xfail, fp_exception_msg),
    ("test_linsolve.py::TestSplu.test_threads_parallel", xfail, thread_msg),
    ("test_propack", skip, todo_signature_mismatch_msg),
    ("test_sparsetools.py::test_threads", xfail, thread_msg),
    # scipy/sparse/csgraph/tests
    ("test_shortest_path.py::test_gh_17782_segfault", xfail, thread_msg),
    # scipy/spatial/tests
    (
        "test_kdtree.py::test_query_ball_point_multithreading",
        xfail,
        thread_msg,
    ),
    ("test_kdtree.py::test_ckdtree_parallel", xfail, thread_msg),
    # scipy/special/tests
    (
        "test_exponential_integrals.py::TestExp1.test_branch_cut",
        xfail,
        "TODO maybe float support since +0 and -0 difference",
    ),
    (
        "test_round.py::test_add_round_(up|down)",
        xfail,
        "TODO small floating point difference, maybe due to lack of floating point "
        "support for controlling rounding, see "
        "https://github.com/WebAssembly/design/issues/1384",
    ),
    # scipy/stats/tests
    (
        "test_continuous_basic.py::test_methods_with_lists.+args96",
        xfail,
        "TODO brentq fails to converge",
    ),
    (
        "test_distributions.py::TestStudentizedRange.test_(cdf|ppf)_against_tables",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        # parametrized tests from 0 to 72, a few pass but xfailing all the test cases for now
        "test_distributions.py::TestStudentizedRange.test_(cdf|pdf)_against_mp",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_distributions.py::TestStudentizedRange.test_pdf_integration",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_distributions.py::TestStudentizedRange.test_cdf_against_r.+r_case_result[01]",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_distributions.py::TestStudentizedRange.test_infinite_df",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_distributions.py::TestStudentizedRange.test_clipping",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_hypotests.py::TestTukeyHSD.test_(compare|engineering_stat_handbook|rand_symm)",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_hypotests.py::TestTukeyHSD.test_2_args_ttest",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_kdeoth.py::test_kde_[12]d",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_multivariate.py::TestMultivariateT.test_cdf_against_generic_integrators",
        skip,
        "TODO tplquad integration does not seem to converge",
    ),
    (
        "test_multivariate.py::TestCovariance.test_mvn_with_covariance_cdf.+Precision-size1",
        xfail,
        "TODO small floating point difference 6e-7 relative diff instead of 1e-7",
    ),
    (
        "test_multivariate.py::TestMultivariateNormal.test_logcdf_default_values",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_multivariate.py::TestMultivariateNormal.test_broadcasting",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_multivariate.py::TestMultivariateNormal.test_normal_1D",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_multivariate.py::TestMultivariateNormal.test_R_values",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_multivariate.py::TestMultivariateNormal.test_cdf_with_lower_limit",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_multivariate.py::TestMultivariateT.test_cdf_against_multivariate_normal",
        xfail,
        todo_genuine_difference_msg,
    ),
    ("test_qmc.py::TestVDC.test_van_der_corput", xfail, thread_msg),
    ("test_qmc.py::TestHalton.test_workers", xfail, thread_msg),
    ("test_qmc.py::TestUtils.test_discrepancy_parallel", xfail, thread_msg),
    (
        "test_qmc.py::TestMultivariateNormalQMC.test_validations",
        xfail,
        "TODO did not raise maybe no floating point exception support?",
    ),
    (
        "test_qmc.py::TestMultivariateNormalQMC.test_MultivariateNormalQMCDegenerate",
        xfail,
        todo_genuine_difference_msg,
    ),
    (
        "test_resampling.+TestMonteCarloHypothesisTest.+test_against_anderson.+logistic",
        skip,
        todo_memory_corruption_msgt,
    ),
    ("test_sampling.py::test_threading_behaviour", xfail, thread_msg),
    ("test_stats.py::TestMGCStat.test_workers", xfail, process_msg),
    (
        "test_stats.py::TestKSTwoSamples.testLargeBoth",
        skip,
        "TODO test taking > 5 minutes after scipy 1.10.1 update",
    ),
    (
        "test_stats.py::TestKSTwoSamples.test_some_code_paths",
        xfail,
        "TODO did not raise maybe no floating point exception support?",
    ),
    (
        "test_stats.py::TestGeometricStandardDeviation.test_raises_value_error",
        xfail,
        "TODO did not raise maybe no floating point exception support?",
    ),
    (
        "test_stats.py::TestBrunnerMunzel.test_brunnermunzel_normal_dist",
        xfail,
        fp_exception_msg,
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
