import daft_lib


def test_add():
    assert daft_lib.add(1, 2) == 3
    assert daft_lib.add(4, 5, 6) == 15


def test_version():
    assert daft_lib.__version__ == "0.0.1"
