# Description

Proof of concept repo to run the scipy tests in Pyodide.

You can run all tests by module like this:
```bash
python run-tests-by-modules.py
```

# Manually curated list of issues

TODO

Some tests need built extension, so scipy-tests is not enough.

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
scipy.integrate._ivp.tests fatal error or timeout (exit code 4)
scipy.integrate.tests fatal error or timeout (exit code 2)
scipy.interpolate.tests fatal error or timeout (exit code None)
scipy.io.arff.tests passed (exit code 0)
scipy.io._harwell_boeing.tests passed (exit code 0)
scipy.io.matlab.tests passed (exit code 0)
scipy.io.tests fatal error or timeout (exit code 2)
scipy._lib.tests fatal error or timeout (exit code 2)
scipy.linalg.tests fatal error or timeout (exit code 7)
scipy.misc.tests passed (exit code 0)
scipy.ndimage.tests failed (exit code 1)
scipy.odr.tests passed (exit code 0)
scipy.optimize.tests fatal error or timeout (exit code 2)
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
scipy.stats.tests fatal error or timeout (exit code None)

--------------------------------------------------------------------------------
Grouped by category:
--------------------------------------------------------------------------------
category failed (4 modules)
    scipy.ndimage.tests
    scipy.sparse.linalg._dsolve.tests
    scipy.sparse.linalg._eigen.arpack.tests
    scipy.special.tests
category fatal error or timeout (14 modules)
    scipy.fft.tests
    scipy.integrate._ivp.tests
    scipy.integrate.tests
    scipy.interpolate.tests
    scipy.io.tests
    scipy._lib.tests
    scipy.linalg.tests
    scipy.optimize.tests
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
```
