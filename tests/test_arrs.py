from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3, 4, 5]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice(array_fixture, -6) == [1, 2, 3, 4, 5]
    assert arrs.my_slice(array_fixture, -3) == [3, 4, 5]
    assert arrs.my_slice(array_fixture, -6, -1) == [2, 3, 4]
