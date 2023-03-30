# Description

Proof of concept repo to run the scipy tests in Pyodide.

You can run all tests by module like this:
```bash
python run-tests-by-modules.py
```

# Manually curated list of issues

## Pyodide fatal error investigation:

- `scipy.linalg` https://github.com/lesteve/scipy-tests-pyodide/pull/2
- `scipy.sparse` https://github.com/lesteve/scipy-tests-pyodide/issues/3
- `scipy.stats` https://github.com/lesteve/scipy-tests-pyodide/pull/4
- `scipy.optimize.tests` https://github.com/lesteve/scipy-tests-pyodide/issues/12

## Pyodide failures investigation

- `scipy.interpolate.tests` https://github.com/lesteve/scipy-tests-pyodide/issues/13
- `scipy.signal.tests` https://github.com/lesteve/scipy-tests-pyodide/pull/5
- `scipy.special.tests` https://github.com/lesteve/scipy-tests-pyodide/issues/15

## Expected failures due to Pyodide limitations

Those tests are marked as xfail in `conftest.py`.

- `scipy.fft.tests` https://github.com/lesteve/scipy-tests-pyodide/pull/7. Test
  failures use threads or multiprocessing.
- `scipy._lib.tests` all tests uses multiprocessing, threads or some fork call https://github.com/lesteve/scipy-tests-pyodide/issues/14
- `scipy.ndimage.tests` test failures use threads
- `scipy.sparse.linalg._dsolve.tests` test failures use threads
- `scipy.sparse.linalg._eigen.arpack.tests` test failures use threads
- `scipy.spatial.tests` https://github.com/lesteve/scipy-tests-pyodide/pull/6.
  Only 4 test failures due to tests creating threads.

## Other issues

Some tests need built extension, that are not built for now in pyodide (see
this
[patch](https://github.com/pyodide/pyodide/blob/main/packages/scipy/patches/0010-skip-fortran-fails-to-link.patch)
for more details). These show up as tests collection error below.

`scipy.integrate._ivp.tests` shows up a pytest usage error because there is no
`__init__.py` for this module.

## Results summary by modules

```
================================================================================
Test results summary
================================================================================
scipy._build_utils.tests passed (exit code 0)
scipy.cluster.tests passed (exit code 0)
scipy.constants.tests passed (exit code 0)
scipy.fftpack.tests passed (exit code 0)
scipy.fft._pocketfft.tests passed (exit code 0)
scipy.fft.tests failed (exit code 1)
scipy.integrate._ivp.tests pytest usage error (exit code 4)
scipy.integrate.tests tests collection error (exit code 2)
scipy.interpolate.tests failed (exit code 1)
scipy.io.arff.tests passed (exit code 0)
scipy.io._harwell_boeing.tests passed (exit code 0)
scipy.io.matlab.tests passed (exit code 0)
scipy.io.tests tests collection error (exit code 2)
scipy._lib.tests failed (exit code 1)
scipy.linalg.tests fatal error or timeout (exit code 66)
scipy.misc.tests passed (exit code 0)
scipy.ndimage.tests failed (exit code 1)
scipy.odr.tests passed (exit code 0)
scipy.optimize.tests fatal error or timeout (exit code None)
scipy.optimize._trustregion_constr.tests passed (exit code 0)
scipy.signal.tests failed (exit code 1)
scipy.sparse.csgraph.tests passed (exit code 0)
scipy.sparse.linalg._dsolve.tests failed (exit code 1)
scipy.sparse.linalg._eigen.arpack.tests failed (exit code 1)
scipy.sparse.linalg._eigen.lobpcg.tests passed (exit code 0)
scipy.sparse.linalg._eigen.tests passed (exit code 0)
scipy.sparse.linalg._isolve.tests fatal error or timeout (exit code 66)
scipy.sparse.linalg.tests fatal error or timeout (exit code 66)
scipy.sparse.tests failed (exit code 1)
scipy.spatial.tests failed (exit code 1)
scipy.spatial.transform.tests passed (exit code 0)
scipy.special.tests failed (exit code 1)
scipy.stats.tests fatal error or timeout (exit code 66)

--------------------------------------------------------------------------------
Grouped by category:
--------------------------------------------------------------------------------
category failed (10 modules)
    scipy.fft.tests
    scipy.interpolate.tests
    scipy._lib.tests
    scipy.ndimage.tests
    scipy.signal.tests
    scipy.sparse.linalg._dsolve.tests
    scipy.sparse.linalg._eigen.arpack.tests
    scipy.sparse.tests
    scipy.spatial.tests
    scipy.special.tests
category fatal error or timeout (5 modules)
    scipy.linalg.tests
    scipy.optimize.tests
    scipy.sparse.linalg._isolve.tests
    scipy.sparse.linalg.tests
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
category tests collection error (2 modules)
    scipy.integrate.tests
    scipy.io.tests
```

### Similar scipy status found in the Pyodide issues

- 16 June 2022 scipy summary:
  https://github.com/pyodide/pyodide/issues/2727#issuecomment-1157866792

- 16 June 2022 sparse is almost passing: 3 failures when using pytest filter
  `not test_cornercase and not iterative and not test_exception`
  https://github.com/pyodide/pyodide/pull/2728#issuecomment-1158010553

