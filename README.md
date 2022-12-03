# Description

Proof of concept repo to run the scipy tests in Pyodide.

You can run all tests by module like this:
```bash
python run-tests-by-modules.py
```

# Manually curated list of issues

TODO: try to reduce fatal error in module tests to smaller snippets.

Some tests need built extension, so scipy-tests is not enough. These show up as
tests collection error below.

`scipy.integrate._ivp.tests` shows up a pytest usage error because there is no
`__init__.py` for this module.

Results summary by modules:

```
================================================================================
Test results summary
================================================================================
scipy._build_utils.tests passed (exit code 0)
scipy.cluster.tests passed (exit code 0)
scipy.constants.tests passed (exit code 0)
scipy.fftpack.tests passed (exit code 0)
scipy.fft._pocketfft.tests passed (exit code 0)
scipy.fft.tests fatal error or timeout (exit code 7)
scipy.integrate._ivp.tests pytest usage error (exit code 4)
scipy.integrate.tests tests collection error (exit code 2)
scipy.interpolate.tests failed (exit code 1)
scipy.io.arff.tests passed (exit code 0)
scipy.io._harwell_boeing.tests passed (exit code 0)
scipy.io.matlab.tests passed (exit code 0)
scipy.io.tests tests collection error (exit code 2)
scipy._lib.tests tests collection error (exit code 2)
scipy.linalg.tests fatal error or timeout (exit code 7)
scipy.misc.tests passed (exit code 0)
scipy.ndimage.tests failed (exit code 1)
scipy.odr.tests passed (exit code 0)
scipy.optimize.tests tests collection error (exit code 2)
scipy.optimize._trustregion_constr.tests passed (exit code 0)
scipy.signal.tests fatal error or timeout (exit code 7)
scipy.sparse.csgraph.tests passed (exit code 0)
scipy.sparse.linalg._dsolve.tests failed (exit code 1)
scipy.sparse.linalg._eigen.arpack.tests failed (exit code 1)
scipy.sparse.linalg._eigen.lobpcg.tests passed (exit code 0)
scipy.sparse.linalg._eigen.tests passed (exit code 0)
scipy.sparse.linalg._isolve.tests fatal error or timeout (exit code 7)
scipy.sparse.linalg.tests fatal error or timeout (exit code 7)
scipy.sparse.tests fatal error or timeout (exit code 7)
scipy.spatial.tests fatal error or timeout (exit code 7)
scipy.spatial.transform.tests passed (exit code 0)
scipy.special.tests failed (exit code 1)
scipy.stats.tests fatal error or timeout (exit code 7)

--------------------------------------------------------------------------------
Grouped by category:
--------------------------------------------------------------------------------
category failed (5 modules)
    scipy.interpolate.tests
    scipy.ndimage.tests
    scipy.sparse.linalg._dsolve.tests
    scipy.sparse.linalg._eigen.arpack.tests
    scipy.special.tests
category fatal error or timeout (8 modules)
    scipy.fft.tests
    scipy.linalg.tests
    scipy.signal.tests
    scipy.sparse.linalg._isolve.tests
    scipy.sparse.linalg.tests
    scipy.sparse.tests
    scipy.spatial.tests
    scipy.stats.tests
category passed (15 modules)
    scipy._build_utils.tests
    scipy.cluster.tests
    scipy.constants.tests
    scipy.fftpack.tests
    scipy.fft._pocketfft.tests
    scipy.io.arff.tests
    scipy.io._harwell_boeing.tests
    scipy.io.matlab.tests
    scipy.misc.tests
    scipy.odr.tests
    scipy.optimize._trustregion_constr.tests
    scipy.sparse.csgraph.tests
    scipy.sparse.linalg._eigen.lobpcg.tests
    scipy.sparse.linalg._eigen.tests
    scipy.spatial.transform.tests
category pytest usage error (1 modules)
    scipy.integrate._ivp.tests
category tests collection error (4 modules)
    scipy.integrate.tests
    scipy.io.tests
    scipy._lib.tests
    scipy.optimize.tests
```

### Similar scipy status found in the Pyodide issues

- 16 June 2022 scipy summary:
  https://github.com/pyodide/pyodide/issues/2727#issuecomment-1157866792

- 16 June 2022 sparse is almost passing: 3 failures when using pytest filter
  `not test_cornercase and not iterative and not test_exception`
  https://github.com/pyodide/pyodide/pull/2728#issuecomment-1158010553

