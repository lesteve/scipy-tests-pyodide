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

See xfailed tests in [conftest.py](./conftest.py).

## Other issues

Some tests need built extension, that are not built for now in pyodide (see
this
[patch](https://github.com/pyodide/pyodide/blob/main/packages/scipy/patches/0010-skip-fortran-fails-to-link.patch)
for more details). These show up as tests collection error below.

`scipy.integrate._ivp.tests` shows up a pytest usage error because there is no
`__init__.py` for this module.

## Results summary by modules

2023-04-18

```
================================================================================
Test results summary
================================================================================
scipy._build_utils.tests pytest usage error (exit code 4), expected ['passed', 'pytest usage error']
scipy.cluster.tests passed (exit code 0), expected ['passed']
scipy.constants.tests passed (exit code 0), expected ['passed']
scipy.fftpack.tests passed (exit code 0), expected ['passed']
scipy.fft._pocketfft.tests passed (exit code 0), expected ['passed']
scipy.fft.tests passed (exit code 0), expected ['passed']
scipy.integrate._ivp.tests pytest usage error (exit code 4), expected ['pytest usage error']
scipy.integrate.tests tests collection error (exit code 2), expected ['tests collection error']
scipy.interpolate.tests failed (exit code 1), expected ['failed']
scipy.io.arff.tests passed (exit code 0), expected ['passed']
scipy.io._harwell_boeing.tests passed (exit code 0), expected ['passed']
scipy.io.matlab.tests passed (exit code 0), expected ['passed']
scipy.io.tests tests collection error (exit code 2), expected ['tests collection error']
scipy._lib.tests passed (exit code 0), expected ['passed']
scipy.linalg.tests passed (exit code 0), expected ['passed']
scipy.misc.tests passed (exit code 0), expected ['passed']
scipy.ndimage.tests passed (exit code 0), expected ['passed']
scipy.odr.tests passed (exit code 0), expected ['passed']
scipy.optimize.tests failed (exit code 1), expected ['failed']
scipy.optimize._trustregion_constr.tests passed (exit code 0), expected ['passed']
scipy.signal.tests failed (exit code 1), expected ['failed']
scipy.sparse.csgraph.tests passed (exit code 0), expected ['passed']
scipy.sparse.linalg._dsolve.tests passed (exit code 0), expected ['passed']
scipy.sparse.linalg._eigen.arpack.tests passed (exit code 0), expected ['passed']
scipy.sparse.linalg._eigen.lobpcg.tests passed (exit code 0), expected ['passed']
scipy.sparse.linalg._eigen.tests passed (exit code 0), expected ['passed']
scipy.sparse.linalg._isolve.tests passed (exit code 0), expected ['passed']
scipy.sparse.linalg.tests passed (exit code 0), expected ['passed']
scipy.sparse.tests passed (exit code 0), expected ['passed']
scipy.spatial.tests passed (exit code 0), expected ['passed']
scipy.spatial.transform.tests passed (exit code 0), expected ['passed']
scipy.special.tests failed (exit code 1), expected ['failed']
scipy.stats.tests failed (exit code 1), expected ['failed']

--------------------------------------------------------------------------------
Grouped by category
--------------------------------------------------------------------------------
category failed (5 modules)
    scipy.interpolate.tests
    scipy.optimize.tests
    scipy.signal.tests
    scipy.special.tests
    scipy.stats.tests
category passed (24 modules)
    scipy.cluster.tests
    scipy.constants.tests
    scipy.fftpack.tests
    scipy.fft._pocketfft.tests
    scipy.fft.tests
    scipy.io.arff.tests
    scipy.io._harwell_boeing.tests
    scipy.io.matlab.tests
    scipy._lib.tests
    scipy.linalg.tests
    scipy.misc.tests
    scipy.ndimage.tests
    scipy.odr.tests
    scipy.optimize._trustregion_constr.tests
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
category pytest usage error (2 modules)
    scipy._build_utils.tests
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

