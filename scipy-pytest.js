const { opendir } = require('node:fs/promises');
const { loadPyodide } = require("pyodide");

async function main() {
  let exit_code = 0;
  try {
    global.pyodide = await loadPyodide();
    let pyodide = global.pyodide;
    const FS = pyodide.FS;
    const NODEFS = FS.filesystems.NODEFS;

    let mountDir = "/mnt";
    pyodide.FS.mkdir(mountDir);
    pyodide.FS.mount(pyodide.FS.filesystems.NODEFS, { root: "." }, mountDir);

    await pyodide.loadPackage(["micropip"]);
    await pyodide.runPythonAsync(`
       import micropip

       await micropip.install(['scipy'])

       pkg_list = micropip.list()
       print(pkg_list)
    `);

    await pyodide.runPythonAsync("import micropip; micropip.install('pytest')");
    // somehow this import is needed not sure why import pytest is not enough...
    await pyodide.runPythonAsync("micropip.install('tomli')");
    let pytest = pyodide.pyimport("pytest");
    let args = process.argv.slice(2);
    console.log('pytest args:', args);
    exit_code = pytest.main(pyodide.toPy(args));
  } catch (e) {
    console.error(e);
    // Arbitrary exit code here. When there is a Pyodide fatal error, we don't
    // get here somehow and the exit code is 7
    exit_code = 66;

  } finally {
    process.exit(exit_code);
  }
}

main();
