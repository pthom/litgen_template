import lg_examplelib


def test_version():
    assert lg_examplelib.__version__ == "0.0.1"


def test_examplelib():
    assert lg_examplelib.add(3, 4) == 7


def test_boxed_type():
    i = lg_examplelib.BoxedInt(3)
    lg_examplelib.inplace_multiply(i)
    assert i.value == 6
