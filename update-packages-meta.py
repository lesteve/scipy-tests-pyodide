from pathlib import Path
import hashlib
import ruamel.yaml
import requests

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

# Unvendor scipy tests
meta_path = Path("packages/scipy/meta.yaml")
meta = yaml.load(meta_path.read_text())
meta["build"]["unvendor-tests"] = False
yaml.dump(meta, meta_path.open("w"))

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
