import sys

try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise

from setuptools import find_packages
setup(
    name="example-lib",
    version="0.0.1",
    description="example-lib, example of bindings with skbuild and litgen",
    author="Pascal Thomet",
    author_email="pthomet@gmail.com",
    url="https://github.com/pthom/litgen",

    packages=(["example_lib"]),
    package_dir={"": "bindings"},
    cmake_install_dir="bindings/example_lib",

    include_package_data=True,
    package_data={"example_lib": ["py.typed", "*.pyi"]},

    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
    install_requires=[],
)
