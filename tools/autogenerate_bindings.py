import litgen
import os


def my_litgen_options() -> litgen.LitgenOptions:
    # configure your options here
    options = litgen.LitgenOptions()

    # The namespace DaftLib is the root namespace for the generated bindings
    # (i.e. no submodule will be generated for it in the python bindings)
    options.namespaces_root = ["DaftLib"]

    # SwitchBoolValue is a C++ function that takes a bool parameter by reference and changes its value
    # Since bool are immutable in python, we can to use a BoxedBool instead
    options.fn_params_replace_modifiable_immutable_by_boxed__regex = "^SwitchBoolValue$"

    # priv_ is a prefix for private functions that we don't want to expose
    options.fn_exclude_by_name__regex = "^priv_"

    # We don't want to expose the private class DaftLib::PrivateClass
    options.fn_params_exclude_names__regex = "^priv_"

    # Widget& GetWidgetSingleton()
    # returns a reference, that python should not free.
    # so we will force the reference policy to be 'reference' instead of 'automatic'
    options.fn_return_force_policy_reference_for_references__regex = "Singleton$"

    # The functions in the MathFunctions namespace will be also published as vectorized functions
    options.fn_namespace_vectorize__regex = r"^DaftLib::MathFunctions$"
    options.fn_vectorize__regex = r".*"

    # The virtual methods of this class can be overriden in python
    options.class_override_virtual_methods_in_python__regex = "^Animal$"

    #  template<typename T> T MaxValue(const std::vector<T>& values);
    # will be published as: max_value_int and max_value_float
    options.fn_template_options.add_specialization("^MaxValue$", ["int", "float"], add_suffix_to_function_name=True)
    #  template<typename T> T MaxValue(const std::vector<T>& values);
    # will be published as: max_value_int and max_value_float
    options.fn_template_options.add_specialization("^MinValue$", ["int", "float"], add_suffix_to_function_name=False)

    # Set to True if you want the stub file to be formatted with black
    options.python_run_black_formatter = True

    return options


def autogenerate() -> None:
    repository_dir = os.path.realpath(os.path.dirname(__file__) + "/../")
    output_dir = repository_dir + "/src/python_bindings"

    include_dir = repository_dir + "/src/cpp_libraries/"
    header_files = [include_dir + "DaftLib/DaftLib.h"]

    litgen.write_generated_code_for_files(
        options=my_litgen_options(),
        input_cpp_header_files=header_files,
        output_cpp_pydef_file=output_dir + "/pybind_DaftLib.cpp",
        output_stub_pyi_file=output_dir + "/daft_lib/__init__.pyi",
    )


if __name__ == "__main__":
    autogenerate()
