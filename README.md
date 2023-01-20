# lg_skuild_template

An adpatation of [scikit_build_example](https://github.com/pybind/scikit_build_example) for [litgen](https://github.com/pthom/litgen)

[![Gitter][gitter-badge]][gitter-link]

|      CI              | status |
|----------------------|--------|
| conda.recipe         | [![Conda Actions Status][actions-conda-badge]][actions-conda-link] |
| pip builds           | [![Pip Actions Status][actions-pip-badge]][actions-pip-link] |


An example project built with [pybind11](https://github.com/pybind/pybind11), 
[scikit-build](https://scikit-build.readthedocs.io/en/latest/), and [litgen](https://github.com/pthom/litgen). 


[gitter-badge]:            https://badges.gitter.im/pybind/Lobby.svg
[gitter-link]:             https://gitter.im/pybind/Lobby
[actions-badge]:           https://github.com/pthom/lg_skbuild_template/workflows/Tests/badge.svg
[actions-conda-link]:      https://github.com/pthom/lg_skbuild_template/actions?query=workflow%3AConda
[actions-conda-badge]:     https://github.com/pthom/lg_skbuild_template/workflows/Conda/badge.svg
[actions-pip-link]:        https://github.com/pthom/lg_skbuild_template/actions?query=workflow%3APip
[actions-pip-badge]:       https://github.com/pthom/lg_skbuild_template/workflows/Pip/badge.svg
[actions-wheels-link]:     https://github.com/pthom/lg_skbuild_template/actions?query=workflow%3AWheels
[actions-wheels-badge]:    https://github.com/pthom/lg_skbuild_template/workflows/Wheels/badge.svg

# Usage

### Step 1: clone this repository

```bash
git clone git@github.com:pthom/lg_skbuild_template.git
cd lg_skbuild_template
```

### Step 2: Customize cpp library name, python package name and pip package name

_(This step is optional if you want to test this template with it default names)_

By default, lg_skbuild_template will use these settings:
* _cpp library name_: a cpp library named "examplelibcpp" (see `external/examplelibcpp`) will be built, 
  and used as a source to generate python bindings.
* _python package name_: a python package named "lg_examplelib" will bind this library  
  This python package include a native module named "_lg_examplelib" which provides the bindings.
* _pip package name_: a pip package named "lg-examplelib" could be published online

Note: "python package name" can in theory be equal to "pip package name", however there is a gotcha: 
*the python package name cannot include "-" (minus), and the pip package name cannot include "_" (underscore)*

> Call `python prepare_template.py` in order to customize this template with your own names. 
This is an interactive program that will ask you for those names and prepare this template for you 
(it will rename files & directories, and do replacements inside files).
_After this, it is advised to remove prepare_template.py and to commit your folder, 
once you made sure that `pip install -v.` works correctly._

__Example session with `python prepare_template.py`__

```
>> python prepare_template.py

* Step 1: enter the name of the cpp library to bind:
a project with this name will be placed inside external/ (you can later replace it with your own)
(in this template, this project is named "examplelibcpp")

    Name of the cpp library to bind: mylib

Step 2: enter the name of the python package 
Note: this name cannot include "-" (i.e. minus) signs
            
    Name of the python package (enter "d" for default, i.e. lg_mylib): d
    Used lg_mylib as python package name!

Step 3: enter the name of the published pip package. This name can be close to the name of the python package.
Note: this name cannot include "_" (i.e. underscore) sign
        
    Name of the pip package (enter "d" for default, i.e. lg-mylib): d
    Used lg-mylib as pip package name!

Please confirm you want to make the modifications (it cannot be undone). Type 'yes' to confirm: yes
```

_After this, you will see various messages explaining what was changed_

### Step 3: autogenerate the binding code 

__First, install litgen__

```
pip install -r requirements-dev.txt
```

__Then run code generation via litgen__
```
python autogenerate_lg_examplelib.py
```

(you might need to replace "autogenerate_lg_examplelib.py" by "autogenerate_{your_python_package_name}.py")

This will:
* Create an amalgamated header file for the library in `mylib_amalgamation.h`
* Write the cpp binding code into `bindings/pybind_mylib.cpp`
* Write the python stub code into `bindings/lg_examplelib/__init__.pyi`

You can of course adapt the code and litgen options inside `autogenerate_lg_examplelib.py`

### Step 4: Check that it works

__First, install the package__
```
pip install -v .
```

__Then, try to import and use it from python__
```python
import lg_examplelib
lg_examplelib.add(1, 2)
```


# CI Examples

There are examples for CI in `.github/workflows`. A simple way to produces
binary "wheels" for all platforms is illustrated in the "wheels.yml" file,
using [`cibuildwheel`][].

# License

pybind11 is provided under a BSD-style license that can be found in the LICENSE
file. By using, distributing, or contributing to this project, you agree to the
terms and conditions of this license.

# Folder structure

## Folder structure

Below is a summary of the folder structure:

```
./
├── pyproject.toml                            # Pip configuration file
├── setup.py                                  # Pip configuration file
├── CMakeLists.txt                            # CMakeLists (used also by pip, via skbuild)
├── requirements-dev.txt
├── Readme.md                                 # This file
├── _skbuild/                                 # Temp build directory when building via pip
│
├── autogenerate_lg_examplelib.py             # This script will read headers in 
│                                             # external/examplelibcpp/include and
│                                             # generate bindings using litgen inside:
│                                             #    - bindings/pybind_examplelibcpp.cpp (C++ publishing code)
│                                             #    - bindings/lg_examplelib/__init__.pyi (stubs)
│
├── bindings/                                 # root of the generated bindings
│         ├── lg_examplelib/
│         │         ├── __init__.py           # The python module main entry point
│         │         ├── __init__.pyi          # Stubs generated by litgen
│         │         └── py.typed              # An empty file that indicates that the python module is typed
│         ├── module.cpp                      # Main entry point of the python module
│         └── pybind_examplelibcpp.cpp        # File with bindings generated by litgen
│
├── lg_cmake_utils/                           # A submodule that contains utilities
│         ├── ...                             # that make it easier to write cmake code for pip modules
│         ├── ...
├── external/
│         ├──examplelibcpp/                   # C++ library that will be wrapped in a python module
│                ├── CMakeLists.txt
│                ├── examplelibcpp.cpp
│                ├── examplelibcpp.h
|                ├── ...
├── examplelibcpp_amalgamation.h              # Autogenerated amalgamated header for examplelibcpp
└── tests/
    ├── basic_test.py                         # This is a list of python tests that will check
    ├── c_string_list_test.py                 #   that the generated python module works as intended.
    ├── c_style_array_test.py
    ├── ...
```


[`cibuildwheel`]:          https://cibuildwheel.readthedocs.io
