import daft_lib


def test_version():
    assert daft_lib.__version__ == "0.0.1"  # type: ignore


def test_daft_lib():
    assert daft_lib.add(3, 4) == 7


def test_boxed_type():
    i = daft_lib.BoxedInt(3)
    daft_lib.inplace_multiply(i)
    assert i.value == 6
