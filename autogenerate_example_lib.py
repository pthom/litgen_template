import os

import litgen


THIS_DIR = os.path.dirname(__file__)
CPP_HEADERS_DIR = THIS_DIR + "/external/example_lib_cpp"
CPP_GENERATED_PYBIND_DIR = THIS_DIR + "/bindings"
assert os.path.isdir(CPP_HEADERS_DIR)
assert os.path.isdir(CPP_GENERATED_PYBIND_DIR)


def autogenerate():
    input_cpp_header = CPP_HEADERS_DIR + "/example_lib_cpp.h"
    output_cpp_pydef_file = CPP_GENERATED_PYBIND_DIR + "/pybind_example_lib_cpp.cpp"
    output_stub_pyi_file = CPP_GENERATED_PYBIND_DIR + "/example_lib_cpp/__init__.pyi"

    # Configure options
    options = litgen.LitgenOptions()
    generated_code = litgen.generate_code(options, filename=input_cpp_header)

    litgen.write_generated_code(
        generated_code,
        output_cpp_pydef_file=output_cpp_pydef_file,
        output_stub_pyi_file=output_stub_pyi_file,
    )


if __name__ == "__main__":
    autogenerate()
