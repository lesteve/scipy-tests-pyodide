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
    # get latest commit from scikit-learn repo
    # curl https://api.github.com/repos/scikit-learn/scikit-learn/commits/main | jq '{message: .commit.message, sha: .sha}'
    last_commit_url = (
        "https://api.github.com/repos/scikit-learn/scikit-learn/commits/main"
    )
    r = requests.get(last_commit_url)
    content = r.json()
    commit_sha = content["sha"]
    commit_message = content["commit"]["message"]
    commit_date = content["commit"]["committer"]["date"]
    print(
        f"got scikit-learn dev from:\n"
        f"message: {commit_message}\n"
        f"commit:  {commit_sha}\n"
        f"date:    {commit_date}"
    )

    url = (
        "https://github.com/scikit-learn/scikit-learn/"
        f"archive/{commit_sha}.zip"
    )
    r = requests.get(url)
    sha256 = hashlib.sha256(r.content).hexdigest()

    meta_path = Path("packages/scikit-learn/meta.yaml")
    meta = yaml.load(meta_path.read_text())

    meta["source"]["url"] = url
    meta["source"]["sha256"] = sha256
    meta["package"]["version"] = f"1.3.0.dev{commit_sha}"
    meta["build"]["unvendor-tests"] = False
    yaml.dump(meta, meta_path.open("w"))


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        args = ["scipy", "scikit-learn"]

    lookup = {"scipy": update_scipy, "scikit-learn": update_scikit_learn}

    for arg in args:
        func = lookup.get(arg)

        if func is None:
            allowed_values = list(lookup.keys())
            raise ValueError(
                f"Could not find package {func_name}. Allowed values are: {allowed_values}"
            )
        func()
