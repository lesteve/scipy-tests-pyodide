from pathlib import Path
import hashlib
import ruamel.yaml
import requests
import sys

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

def update_scipy():
    # Unvendor scipy tests
    meta_path = Path("packages/scipy/meta.yaml")
    meta = yaml.load(meta_path.read_text())
    meta["build"]["unvendor-tests"] = False
    yaml.dump(meta, meta_path.open("w"))

def update_scikit_learn():
    # Use scikit-learn development version and unvendor tests
    url = "https://github.com/scikit-learn/scikit-learn/archive/refs/heads/main.zip"
    r = requests.get(url)
    sha256 = hashlib.sha256(r.content).hexdigest()

    meta_path = Path("packages/scikit-learn/meta.yaml")
    meta = yaml.load(meta_path.read_text())

    meta["source"]["url"] = url
    meta["source"]["sha256"] = sha256
    meta["package"]["version"] = "1.3.0.dev"
    meta["build"]["unvendor-tests"] = False
    yaml.dump(meta, meta_path.open("w"))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError(
            f"Usage: {sys.argv[0]} package"
        )

    lookup = {"scipy": update_scipy, "scikit-learn": update_scikit_learn}
    arg = sys.argv[1]

    func = lookup.get(arg)

    if func is None:
        allowed_values = list(lookup.keys())
        raise ValueError(
            f"Could not find package {func_name}. Allowed values are: {allowed_values}"
        )

    func()
