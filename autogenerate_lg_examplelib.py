import os

import litgen
from litgen.make_amalgamated_header import AmalgamationOptions, write_amalgamate_header_file


THIS_DIR = os.path.dirname(__file__)
EXTERNAL_DIR = THIS_DIR + "/external"
CPP_LIB_DIR = EXTERNAL_DIR + "/examplelibcpp"
CPP_GENERATED_PYBIND_DIR = THIS_DIR + "/bindings"
assert os.path.isdir(CPP_LIB_DIR)
assert os.path.isdir(CPP_GENERATED_PYBIND_DIR)


def make_amalgamated_header():
    options = AmalgamationOptions()

    options.base_dir = EXTERNAL_DIR
    options.local_includes_startwith = "examplelibcpp/"
    options.include_subdirs = ["examplelibcpp"]
    options.main_header_file = "examplelibcpp.h"
    options.dst_amalgamated_header_file = THIS_DIR + "/examplelibcpp_amalgamation.h"

    write_amalgamate_header_file(options)


def autogenerate():
    input_cpp_header = THIS_DIR + "/examplelibcpp_amalgamation.h"
    output_cpp_pydef_file = CPP_GENERATED_PYBIND_DIR + "/pybind_examplelibcpp.cpp"
    output_stub_pyi_file = CPP_GENERATED_PYBIND_DIR + "/lg_examplelib/__init__.pyi"

    # Configure options
    options = litgen.LitgenOptions()
    generated_code = litgen.generate_code(options, filename=input_cpp_header)

    litgen.write_generated_code(
        generated_code,
        output_cpp_pydef_file=output_cpp_pydef_file,
        output_stub_pyi_file=output_stub_pyi_file,
    )


if __name__ == "__main__":
    make_amalgamated_header()
    autogenerate()
