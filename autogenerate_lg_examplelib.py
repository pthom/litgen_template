import os

from codemanip import amalgamated_header

import litgen


THIS_DIR = os.path.dirname(__file__)
EXTERNAL_DIR = THIS_DIR + "/external"
CPP_LIB_DIR = EXTERNAL_DIR + "/examplelibcpp"
CPP_GENERATED_PYBIND_DIR = THIS_DIR + "/bindings"
assert os.path.isdir(CPP_LIB_DIR)
assert os.path.isdir(CPP_GENERATED_PYBIND_DIR)


def make_amalgamated_header():
    options = amalgamated_header.AmalgamationOptions()

    options.base_dir = EXTERNAL_DIR
    options.local_includes_startwith = "examplelibcpp/"
    options.include_subdirs = ["examplelibcpp"]
    options.main_header_file = "examplelibcpp.h"
    options.dst_amalgamated_header_file = THIS_DIR + "/examplelibcpp_amalgamation.h"

    amalgamated_header.write_amalgamate_header_file(options)


def autogenerate():
    output_cpp_pydef_file = CPP_GENERATED_PYBIND_DIR + "/pybind_examplelibcpp.cpp"
    output_stub_pyi_file = CPP_GENERATED_PYBIND_DIR + "/lg_examplelib/__init__.pyi"

    # Configure options
    options = litgen.LitgenOptions()
    # configure your options here
    options.namespace_root__regex = "^examplelib$"
    options.fn_params_replace_modifiable_immutable_by_boxed__regex = "^inplace"

    # We demonstrate here two methods for generating bindings (both of them work correctly):
    # - either using an amalgamated header
    # - or by providing a list of files to litgen
    use_amalgamated_header = False
    if use_amalgamated_header:
        make_amalgamated_header()
        input_cpp_header = THIS_DIR + "/examplelibcpp_amalgamation.h"
        litgen.write_generated_code_for_file(
            options,
            input_cpp_header_file=input_cpp_header,
            output_cpp_pydef_file=output_cpp_pydef_file,
            output_stub_pyi_file=output_stub_pyi_file)
    else:
        include_dir = THIS_DIR + "/external/examplelibcpp"
        header_files = [include_dir + "/examplelibcpp.h", include_dir + "/examplelibcpp_2.h"]
        litgen.write_generated_code_for_files(
            options, header_files, output_cpp_pydef_file, output_stub_pyi_file)


if __name__ == "__main__":
    autogenerate()
