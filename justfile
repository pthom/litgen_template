# List all command
default:
    just --list


# Build the python bindings with pybind11 and run the tests
pybind_test:
    export LITGEN_USE_NANOBIND=OFF && python tools/autogenerate_bindings.py && pip install -v . && pytest tests

# Build the python bindings with nanobind and run the tests
nanobind_test:
    export LITGEN_USE_NANOBIND=ON && python tools/autogenerate_bindings.py && pip install -v . && pytest tests
