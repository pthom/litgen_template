from __future__ import annotations
import os
from dataclasses import dataclass


@dataclass
class PackageNames:
    # Name of the cpp library to bind
    cpp_library_name = "DaftLib"

    # Name of the python module that will bind the cpp library
    # Following the python conventions, module names are preferably snake_case (and cannot contain "-")
    python_module_name = "daft_lib"

    # Name of the pip package that will be published:
    # it can be close to the python module name, but it cannot contain underscores "_" !
    pip_package_name = "daft-lib"

    @staticmethod
    def _template_default_package_names() -> PackageNames:
        r = PackageNames()
        return r

    @staticmethod
    def _empty_package_names() -> PackageNames:
        r = PackageNames()
        r.cpp_library_name = ""
        r.python_module_name = ""
        r.pip_package_name = ""
        return r

    def replace_in_string(self, s: str) -> str:
        default_names = PackageNames._template_default_package_names()
        r = s
        r = r.replace(default_names.cpp_library_name, self.cpp_library_name)
        r = r.replace(default_names.python_module_name, self.python_module_name)
        r = r.replace(default_names.pip_package_name, self.pip_package_name)
        return r

    def replace_in_file(self, filename: str) -> None:
        valid_extensions = [
            "py",
            "cpp",
            "h",
            "pyi",
            "txt",
            "toml",
            "ini",
            "yaml",
            "md",
            "yml",
        ]
        ok = False
        for extension in valid_extensions:
            if filename.endswith(extension):
                ok = True
        if not ok:
            print(f"skipping {filename}")
            return

        print(f"_replace_in_file {filename}")

        with open(filename, "r") as input_file:
            content = input_file.read()
            content = self.replace_in_string(content)

        with open(filename, "w") as outputfile:
            outputfile.write(content)

    def replace_in_files(self) -> None:
        default_names = PackageNames._template_default_package_names()
        # Directories where to replace by the new names:
        directories = [
            ".github/workflows",
            "./tools",
            "./_pydef_nanobind",
            "./_pydef_pybind11",
            f"./_stubs/{default_names.python_module_name}",
            f"./src/cpp_libraries/{default_names.cpp_library_name}",
            f"./src/cpp_libraries/{default_names.cpp_library_name}/cpp",
            "./conda.recipe",
            "./tests",
            ".",
        ]

        for directory in directories:
            files = os.listdir(f"{directory}")
            for file in files:
                file_fullpath = f"{directory}/{file}"
                if os.path.isfile(file_fullpath):
                    is_excluded = False
                    if file == "change_lib_name.py":
                        is_excluded = True
                    if file.endswith(".md"):
                        is_excluded = True
                    if not is_excluded:
                        self.replace_in_file(file_fullpath)

    def rename_files(self) -> None:
        """
        Directories and files to rename:
            ./src/python_bindings/daft_lib
            ./src/cpp_libraries/DaftLib
            ./src/cpp_libraries/DaftLib/DaftLib.h
            ./src/cpp_libraries/DaftLib/cpp/DaftLib.cpp
            ./tests/daft_lib_test.py
        """
        default_names = PackageNames._template_default_package_names()
        dir_and_files_to_rename = [
            f"./_stubs/{default_names.python_module_name}/",
            f"./_pydef_nanobind/nanobind_{default_names.cpp_library_name}.cpp",
            f"./_pydef_pybind11/pybind_{default_names.cpp_library_name}.cpp",
            f"./src/cpp_libraries/{default_names.cpp_library_name}/",
            f"tests/{default_names.python_module_name}_test.py",
        ]

        for pathname in dir_and_files_to_rename:
            new_pathname = self.replace_in_string(pathname)
            src = f"{pathname}"
            dst = f"{new_pathname}"
            print(f"os.rename({src}, {dst})")
            os.rename(src, dst)

        default_names = PackageNames()
        os.rename(
            f"src/cpp_libraries/{self.cpp_library_name}/{default_names.cpp_library_name}.h",
            f"src/cpp_libraries/{self.cpp_library_name}/{self.cpp_library_name}.h",
        )
        os.rename(
            f"src/cpp_libraries/{self.cpp_library_name}/cpp/{default_names.cpp_library_name}.cpp",
            f"src/cpp_libraries/{self.cpp_library_name}/cpp/{self.cpp_library_name}.cpp",
        )

    def do_replace(self) -> None:
        self.replace_in_files()
        self.rename_files()

    @staticmethod
    def from_user_input() -> PackageNames:
        r = PackageNames._empty_package_names()

        step1_help = """
* Step 1: enter the name of the cpp library to bind (in this template, it is named "DaftLib"):
a project with this name will be placed inside src/cpp_libraries/ (you can later replace it with your own)

"""
        step2_help = """
Step 2: Name of the python module that will bind the cpp library (in this template, it is named "daft_lib")
Following the python conventions, module names are preferably snake_case (and cannot contain "-")
Note: two python modules will be created:
    - one with the name you give here (it is a python interface to the native module)
    - one with the name you give here, prefixed by "_" (it is the native module)
            """
        step3_help = """
Step 3: enter the name of the python pip package package (in this template, it is named "daft-lib")
This name can be close to the name of the python package, but can't include "_" (i.e. underscore) sign
        """

        # Step 1: ask for cpp library name
        while len(r.cpp_library_name) == 0:
            print(step1_help)
            r.cpp_library_name = input("    Name of the cpp library to bind: ")

        # Step 2: ask for python package name
        while len(r.python_module_name) == 0:
            default_python_package_name = r.cpp_library_name
            print(step2_help)
            r.python_module_name = input(
                f'    Name of the python module (enter "d" for default, i.e. {default_python_package_name}): '
            )
            if r.python_module_name.lower() == "d":
                r.python_module_name = default_python_package_name
                print(f"    Used {default_python_package_name} as python package name!")

        # Step 3: ask for pip package name
        while len(r.pip_package_name) == 0:
            default_pip_package_name = r.python_module_name.replace("_", "-")
            print(step3_help)
            r.pip_package_name = input(
                f'    Name of the pip package (enter "d" for default, i.e. {default_pip_package_name}): '
            )
            if r.pip_package_name.lower() == "d":
                r.pip_package_name = default_pip_package_name
                print(f"    Used {default_pip_package_name} as pip package name!")

        return r


def main() -> None:
    repo_dir = os.path.dirname(os.path.realpath(__file__ + "/../../"))
    os.chdir(repo_dir)
    interactive = True
    if interactive:
        package_names = PackageNames.from_user_input()
        answer = input(
            "\nPlease confirm you want to make the modifications (it cannot be undone). Type 'yes' to confirm: "
        )
        if answer != "yes":
            print("Cancelled!")
            return
    else:
        package_names = PackageNames()
        package_names.cpp_library_name = "..."
        package_names.python_module_name = "..."
        package_names.pip_package_name = "..."
        raise NotImplementedError("Please fill in the names in the code")

    package_names.do_replace()


if __name__ == "__main__":
    main()
