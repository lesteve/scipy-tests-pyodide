# Description

2024-07-17: the scipy tests with `-m 'not slow'` are now run in the Pyodide
repo, this repo is less relevant.

See https://github.com/pyodide/pyodide/pull/4935 for the PR that added scipy
tests in Pyodide.

See [scipy-conftest.py](https://github.com/pyodide/pyodide/blob/main/packages/scipy/scipy-conftest.py)
for skipped and xfailed tests in scipy.

See `test-scipy` job in Pyodide [GHA
workflow](https://github.com/pyodide/pyodide/blob/main/.github/workflows/main.yml)
to see how the Scipy tests are run inside Pyodide with node.

# Manually curated list of issues

Not updated very often, I should do some kind of high-level summary one day ...

https://hackmd.io/9cbsykxyT9mstqfW0EV5ug?viewk

# Running locally

You can run all tests by module like this:
```bash
python run-tests-by-modules.py
```

