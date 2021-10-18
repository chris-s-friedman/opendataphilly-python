from os import path

from setuptools import find_packages, setup

# requirements from requirements.txt
root_dir = path.dirname(path.abspath(__file__))
with open(path.join(root_dir, "requirements.txt"), "r") as f:
    requirements = f.read().splitlines()

# long description from README
with open(path.join(root_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="odphilly-tools",
    use_scm_version={
        "local_scheme": "dirty-tag",
        "version_scheme": "post-release",
    },
    setup_requires=["setuptools_scm"],
    description="Reusable OpenDataPhilly python utilities",
    author="Chris Friedman",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chris-s-friedman/opendataphilly-python",
    packages=find_packages(),
    python_requires=">=3.9, <4",
    install_requires=requirements,
)
