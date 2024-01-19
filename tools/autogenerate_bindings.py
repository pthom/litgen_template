import litgen
import os


def my_litgen_options() -> litgen.LitgenOptions:
    options = litgen.LitgenOptions()
    # configure your options here
    options.namespace_root__regex = "^DaftLib$"
    options.fn_params_replace_modifiable_immutable_by_boxed__regex = "^inplace"
    return options


def autogenerate():
    repository_dir = os.path.realpath(os.path.dirname(__file__) + "/../")
    output_dir = repository_dir + "/bindings"

    include_dir = repository_dir + "/cpp_libs/"
    header_files = [include_dir + "DaftLib/DaftLib.h"]

    litgen.write_generated_code_for_files(
        options=my_litgen_options(),
        input_cpp_header_files=header_files,
        output_cpp_pydef_file=output_dir + "/pybind_DaftLib.cpp",
        output_stub_pyi_file=output_dir + "/daft_lib/__init__.pyi"
    )


if __name__ == "__main__":
    autogenerate()
