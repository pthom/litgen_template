# litgen template

A template repository to build python bindings using [litgen](https://pthom.github.io/litgen), and [scikit-build](https://scikit-build-core.readthedocs.io/en/latest/getting_started.html). 

This template is based on [scikit_build_example](https://github.com/pybind/scikit_build_example).


## Usage for final users

### First, install the package
```bash
git clone https://github.com/pthom/litgen_template.git && cd litgen_template
pip install -v .
```

### Then, use it from python
```python
import daft_lib
daft_lib.add(1, 2)
```
(this template builds bindings for a C++ library called DaftLib, and publishes it as a python module called daft_lib)


## Development mode for C++

If you want to quickly iterate on the C++ code, and see the changes reflected in python without having to reinstall the package, you should **not** use python editable development mode. Instead, follow the instruction below.

### Setup C++ development mode

#### Step1: Install the package normally with
```bash
pip install -v .
```
(do **not** install the package in editable mode with `pip install -v -e .`)

#### Step 2: Create a standard C++ build directory:
```bash
mkdir build && cd build
cmake ..
make # rebuild when you change the C++ code, and the changes will be reflected in python!
```

#### Step 3: Change the C++ code, and rebuild the C++ code

Your changes will be reflected in python without having to reinstall the package, since CMakes will automatically copy the native module to the python package folder.

### Debug C++  bindings in editable mode

The [pybind_native_debug](https://github.com/pthom/litgen_template/blob/master/pybind_native_debug) executable provided in this template
is a simple C++ program that can be used to debug the bindings in editable mode.

```
src/pybind_native_debug/
        ├── CMakeLists.txt
        ├── pybind_native_debug.cpp
        ├── pybind_native_debug.py
        ├── pybind_native_debug_venv.txt
        └── pybind_native_debug_venv.txt.example
```

#### Step 1: edit `pybind_native_debug_venv.txt`
Create a file `pybind_native_debug/pybind_native_debug_venv.txt`, and add the path to the python virtual environment that you want to use to debug the bindings.

#### Step 2: edit `pybind_native_debug.py`
Simply edit the python file `pybind_native_debug.py` by adding calls to the functions you want to debug. Then, place breakpoints in the C++ code, and run the program.

### About python editable mode

The python editable mode is intended to quickly iterate on the python code, without having to reinstall the package.

In the case of this template, we are interested in iterating on the C++ code. 
Therefore, we do not use (and do not support) the python editable mode.


----------------

## How-to generate the binding code

### Step 1: Install requirements

#### Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Install the requirements

```
pip install -r requirements-dev.txt
```
This will install [litgen](https://pthom.github.io/litgen) (the bindings generator), [pybind11](https://pybind11.readthedocs.io/en/stable/) (a library to create C++ to Python bindings), [pytest](https://docs.pytest.org) (for the tests), [black](https://black.readthedocs.io/en/stable/index.html) (a code formatter), and [mypy](https://www.mypy-lang.org/) (static type checker for python).

**Install srcML separately (srcML is required by litgen)**

Follow the [instructions on the litgen website](https://pthom.github.io/litgen/litgen_book/01_05_10_install.html) 

### Step 2: (re)generate bindings for your code

#### Optionally, change the C++ code
- Change the C++ code (add functions, etc.) in [src/cpp_libraries/DaftLib/DaftLib.h](https://github.com/pthom/litgen_template/tree/master/src/cpp_libraries/DaftLib/DaftLib.h) and [src/cpp_libraries/DaftLib/cpp/DaftLib.cpp](https://github.com/pthom/litgen_template/blob/master/src/cpp_libraries/DaftLib/cpp/DaftLib.cpp)
- Adapt the generation options inside [tools/autogenerate_bindings.py](https://github.com/pthom/litgen_template/blob/master/tools/autogenerate_bindings.py)

#### Run the code generation via litgen:

```
python tools/autogenerate_bindings.py
```

This will:
* Write the cpp binding code into [src/python_bindings/pybind_DaftLib.cpp](https://github.com/pthom/litgen_template/blob/master/src/python_bindings/pybind_DaftLib.cpp)
* Write the python stubs (i.e. typed declarations) into [src/python_bindings/daft_lib/__init__.pyi](https://github.com/pthom/litgen_template/blob/master/src/python_bindings/daft_lib/__init__.pyi)

#### Build the python module

```bash
pip install -v .
``` 

----------------

## How-to generate bindings for you own library

### Names, names, names

In this template repository:
- the C++ library is called `DaftLib`
- the native python module generated by pybind11 is called `_daft_lib`
- the python module which is imported by users is called `daft_lib` (it imports and optionally adapts `_daft_lib`)
- the pip package that can optionally be published to PyPI is called `daft-lib` (as Pypi does not allow dashes in package names)

You can change these names by running `tools/change_lib_name/change_lib_name.py` once after cloning this template.

----------------

### Structure of this template

#### Bound C++ library
The C++ library `DaftLib` is stored inside src/cpp_libraries/DaftLib/

```
src/cpp_libraries/
└── DaftLib/
    ├── CMakeLists.txt
    ├── DaftLib.h
    └── cpp/
        └── DaftLib.cpp
```

#### Python bindings

The python bindings are stored inside `src/python_bindings/`

```
src/python_bindings/
  ├─── module.cpp              # Main entry point of the python module
  │── pybind_DaftLib.cpp       # File with bindings *generated by litgen*
  │
  ├─ daft_lib/
  │    ├── __init__.pyi        # Stubs *generated by litgen*
  │    ├── __init__.py         # The python module (daft_lib) main entry point
  │    │                       # (it imports and optionally adapts _daft_lib)
  │    ├── py.typed            # An empty file that indicates that the python module is typed
  │    │
  │    └── _daft_lib.xxx.so*   # (optional: the native _daftlib module generated by pybind11,
  │                            #  only present in editable mode)
  ├── daft_lib.egg-info/       # (optional: metadata for the pip package, only present in editable mode)
```

#### Tooling for the bindings generation
```
tools/
├── autogenerate_bindings.py
└── change_lib_name/
    └── change_lib_name.py
```

`tools/autogenerate_bindings.py` is the script that will generate the bindings using litgen.

`tools/change_lib_name/change_lib_name.py` is an optional utility that you can use once after cloning this template,
in order to rename the libraries (e.g. from `DaftLib` to `MyLib`, `daft_lib` to `my_lib`, etc.)


#### Compilation

```
├── CMakeLists.txt                 # CMakeLists (used also by pip, via skbuild)
├── litgen_cmake/                  # litgen_setup_module() is a cmake function that simplifies
│   └── litgen_setup_module.cmake  # the deployment of a python module with litgen
│
├── requirements-dev.txt           # Requirements for development (litgen, pybind11, pytest, black, mypy)
│
├── _skbuild/                      # Temp build directory when building via pip
                                   # (you may have to remove this folder to generate clean builds) 
```

#### Deployment

```
├── pyproject.toml
├── setup.py
```

`pyproject.toml` and `setup.py` are the files that are used by pip to build and deploy the package.
They define the name of the package, the version, the dependencies, etc.


#### CI

```
.github/
├── dependabot.yml   # Configuration for dependabot (automatically update CI dependencies)
├── workflows/
    ├── conda.yml    # Build the package with conda
    ├── pip.yml      # Build the package with pip
    └── wheels.yml   # Build the wheels with cibuildwheel, and publish them to PyPI
                     # (when a new release is created on github)
```

Note: 
- cibuildwheel is configurable via options defined in the pyproject.toml file: see the `[tool.cibuildwheel]` section.
- it is also configurable via environment variables, see [cibuildwheel documentation](https://cibuildwheel.readthedocs.io/en/stable/options/)

#### Tests

```
├── tests/daft_lib_test.py    # This is a list of python tests that will check
└── pytest.ini
```

Those tests are run by cibuildwheel and by the pip CI workflow.