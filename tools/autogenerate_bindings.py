import litgen
import os


def my_litgen_options() -> litgen.LitgenOptions:
    options = litgen.LitgenOptions()
    # configure your options here
    options.namespace_root__regex = "^examplelib$"
    options.fn_params_replace_modifiable_immutable_by_boxed__regex = "^inplace"
    return options


def autogenerate():
    repo_dir = os.path.dirname(__file__ + "/../")
    output_dir = repo_dir + "/bindings"

    include_dir = repo_dir + "/external/examplelibcpp"
    header_files = [include_dir + "/examplelibcpp.h", include_dir + "/examplelibcpp_2.h"]

    litgen.write_generated_code_for_files(
        options = my_litgen_options(),
        input_cpp_header_files=header_files,
        output_cpp_pydef_file=output_dir + "/pybind_examplelibcpp.cpp",
        output_stub_pyi_file=output_dir + "/lg_examplelib/__init__.pyi"
    )


if __name__ == "__main__":
    autogenerate()
