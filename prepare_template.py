from __future__ import annotations
import os
from dataclasses import dataclass


_THIS_DIR = os.path.dirname(os.path.realpath(__file__))


@dataclass
class PackageNames:
    """
    By default, lg_skbuild_template will use the following names:
        * The library for which we build bindings is "example_lib_cpp"
        * The name of the python package that binds this library is "example_lib" (this name cannot include "-").
          This python package include a native module named "_example_lib" which provides the bindings.
        * The name of the pip package is "example-lib" (this name cannot include "_")
          (the pip package name can be slightly different from the python package name)
    """
    cpp_library_name = "example_lib_cpp"
    python_package_name = "example_lib"
    pip_package_name = "example-lib"

    def replace_in_string(self, s: str) -> str:
        default_names = PackageNames()
        r = s
        r = r.replace(default_names.cpp_library_name, self.cpp_library_name)
        r = r.replace(default_names.python_package_name, self.python_package_name)
        r= r.replace(default_names.pip_package_name, self.pip_package_name)
        return r

    def replace_in_file(self, filename: str):
        valid_extensions = ["py", "cpp", "h", "pyi", "txt", "toml", "ini", "yaml", "md", "yml"]
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
        # Directories where to replace by the new names:
        directories = [
            "./github/workflows",
            "./bindings",
            "./bindings/example_lib",
            "./external/example_lib_cpp",
            "./conda.recipe",
            "./tests",
            ".",
        ]

        for directory in directories:
            files = os.listdir(f"{_THIS_DIR}/{directory}")
            for file in files:
                file_fullpath = f"{_THIS_DIR}/{directory}/{file}"
                if os.path.isfile(file_fullpath) and file != "prepare_template.py":
                    self.replace_in_file(file_fullpath)

    def rename_files(self) -> None:
        """
        Directories and files to rename:
            ./bindings/example_lib
            ./external/example_lib_cpp
            ./external/example_lib_cpp/example_lib_cpp.h
            ./external/example_lib_cpp/example_lib_cpp.cpp
            ./external/example_lib_cpp/example_lib_cpp_2.h
            ./external/example_lib_cpp/example_lib_cpp_2.cpp
            ./tests/example_lib_test.py
            autogenerate_example_lib.py
        """
        dir_and_files_to_rename = [
            "./bindings/example_lib/",
            "./bindings/pybind_example_lib_cpp.cpp",

            "./external/example_lib_cpp/",

            "autogenerate_example_lib.py",
            "example_lib_cpp_amalgamation.h",

            "tests/example_lib_test.py"
        ]

        for pathname in dir_and_files_to_rename:
            new_pathname = self.replace_in_string(pathname)
            src = f"{_THIS_DIR}/{pathname}"
            dst = f"{_THIS_DIR}/{new_pathname}"
            print(f"os.rename({src}, {dst})")
            os.rename(src, dst)

        default_names = PackageNames()
        os.rename(
            f"{_THIS_DIR}/external/{self.cpp_library_name}/{default_names.cpp_library_name}.h",
            f"{_THIS_DIR}/external/{self.cpp_library_name}/{self.cpp_library_name}.h")
        os.rename(
            f"{_THIS_DIR}/external/{self.cpp_library_name}/{default_names.cpp_library_name}.cpp",
            f"{_THIS_DIR}/external/{self.cpp_library_name}/{self.cpp_library_name}.cpp")
        os.rename(
            f"{_THIS_DIR}/external/{self.cpp_library_name}/{default_names.cpp_library_name}_2.h",
            f"{_THIS_DIR}/external/{self.cpp_library_name}/{self.cpp_library_name}_2.h")
        os.rename(
            f"{_THIS_DIR}/external/{self.cpp_library_name}/{default_names.cpp_library_name}_2.cpp",
            f"{_THIS_DIR}/external/{self.cpp_library_name}/{self.cpp_library_name}_2.cpp")

    def do_replace(self) -> None:
        self.replace_in_files()
        self.rename_files()

    @staticmethod
    def help():
        help_prepare = PackageNames.__doc__ + """

        This utility will make the modifications in order to use new names (replace in files, rename files & folders).
        """
        print(help_prepare)

    @staticmethod
    def from_user_input() -> PackageNames:
        r = PackageNames()
        r.cpp_library_name = input(f"Name of the cpp library to bind (default {r.cpp_library_name}): ")
        r.python_package_name = input(
            f"Name of the python package (default {r.python_package_name}, cannot include \"-\"): ")
        r.pip_package_name = input(
            f"Name of the pip package (default {r.python_package_name}, cannot include \"_\"): ")
        return r


def main():
    interactive = True
    if interactive:
        PackageNames.help()

        package_names = PackageNames.from_user_input()
        answer = input(
            "Please confirm you want to make the modifications (it cannot be undone). Type 'yes' to confirm: ")
        if answer != "yes":
            print("Cancelled!")
            return
    else:
        package_names = PackageNames()
        package_names.cpp_library_name = "..."
        package_names.python_package_name = "..."
        package_names.pip_package_name = "..."
        raise NotImplementedError("Please fill in the names in the code")

    package_names.do_replace()


if __name__ == "__main__":
    main()

