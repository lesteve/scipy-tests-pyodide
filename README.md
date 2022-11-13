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
scipy._build_utils passed (exit code 0)
scipy.cluster passed (exit code 0)
scipy.constants passed (exit code 0)
scipy.fftpack passed (exit code 0)
scipy.fft._pocketfft passed (exit code 0)
scipy.fft fatal error or timeout (exit code 7)
scipy.integrate._ivp fatal error or timeout (exit code 4)
scipy.integrate fatal error or timeout (exit code 2)
scipy.interpolate fatal error or timeout (exit code None)
scipy.io.arff passed (exit code 0)
scipy.io._harwell_boeing passed (exit code 0)
scipy.io.matlab passed (exit code 0)
scipy.io fatal error or timeout (exit code 2)
scipy._lib fatal error or timeout (exit code 2)
scipy.linalg fatal error or timeout (exit code 7)
scipy.misc passed (exit code 0)
scipy.ndimage failed (exit code 1)
scipy.odr passed (exit code 0)
scipy.optimize fatal error or timeout (exit code 2)
scipy.optimize._trustregion_constr passed (exit code 0)
scipy.signal fatal error or timeout (exit code 7)
scipy.sparse.csgraph passed (exit code 0)
scipy.sparse.linalg._dsolve failed (exit code 1)
scipy.sparse.linalg._eigen.arpack failed (exit code 1)
scipy.sparse.linalg._eigen.lobpcg passed (exit code 0)
scipy.sparse.linalg._eigen passed (exit code 0)
scipy.sparse.linalg._isolve fatal error or timeout (exit code 7)
scipy.sparse.linalg fatal error or timeout (exit code 7)
scipy.sparse fatal error or timeout (exit code 7)
scipy.spatial fatal error or timeout (exit code 7)
scipy.spatial.transform passed (exit code 0)
scipy.special failed (exit code 1)
scipy.stats fatal error or timeout (exit code None)

--------------------------------------------------------------------------------
Grouped by category:
--------------------------------------------------------------------------------
category failed (4 modules)
    scipy.ndimage
    scipy.sparse.linalg._dsolve
    scipy.sparse.linalg._eigen.arpack
    scipy.special
category fatal error or timeout (14 modules)
    scipy.fft
    scipy.integrate._ivp
    scipy.integrate
    scipy.interpolate
    scipy.io
    scipy._lib
    scipy.linalg
    scipy.optimize
    scipy.signal
    scipy.sparse.linalg._isolve
    scipy.sparse.linalg
    scipy.sparse
    scipy.spatial
    scipy.stats
category passed (15 modules)
    scipy._build_utils
    scipy.cluster
    scipy.constants
    scipy.fftpack
    scipy.fft._pocketfft
    scipy.io.arff
    scipy.io._harwell_boeing
    scipy.io.matlab
    scipy.misc
    scipy.odr
    scipy.optimize._trustregion_constr
    scipy.sparse.csgraph
    scipy.sparse.linalg._eigen.lobpcg
    scipy.sparse.linalg._eigen
    scipy.spatial.transform
```
