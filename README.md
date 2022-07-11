lg_skuild_template
==============

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

Installation
------------

- clone this repository
- `cd lg_skbuild_template`
- `pip install .`

Customize library name, python package name and pip package name
------------

By default, lg_skbuild_template will use the following names:
* The library for which we build bindings is "example_lib_cpp"
* The name of the python package that binds this library is "example_lib" (this name cannot include "-").
  This python package include a native module named "_example_lib" which provides the bindings.
* The name of the pip package is "example-lib" (this name cannot include "_")
  (the pip package name can be slightly different from the python package name)

Call `python prepare_template.py` in order to customize this template with your own names. This will replace in files, 
and rename files and folders accordingly.

CI Examples
-----------

There are examples for CI in `.github/workflows`. A simple way to produces
binary "wheels" for all platforms is illustrated in the "wheels.yml" file,
using [`cibuildwheel`][].

License
-------

pybind11 is provided under a BSD-style license that can be found in the LICENSE
file. By using, distributing, or contributing to this project, you agree to the
terms and conditions of this license.

Test call
---------

```python
import example_lib
example_lib.add(1, 2)
```

[`cibuildwheel`]:          https://cibuildwheel.readthedocs.io
