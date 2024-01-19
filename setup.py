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


setup(
    name="daft-lib",
    version="0.0.1",
    description="daft-lib, example of bindings with skbuild and litgen",
    long_description="...",
    author="Pascal Thomet",
    author_email="pthomet@gmail.com",
    url="https://github.com/pthom/litgen",
    packages=(["daft_lib"]),
    package_dir={"": "bindings"},
    cmake_install_dir="bindings/daft_lib",
    # include_package_data=True,
    package_data={"daft_lib": ["py.typed", "*.pyi"]},
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
    install_requires=[],
)
