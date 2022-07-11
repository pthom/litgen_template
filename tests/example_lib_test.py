import example_lib


def test_version():
    assert example_lib.__version__ == "0.0.1"


def test_examplelib():
    assert example_lib.add(3, 4) == 7
