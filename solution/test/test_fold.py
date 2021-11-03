import pytest

from solution.src.fold import fold


def add(a: float, b: float) -> float:
    return a + b


def multiply(a: float, b: float) -> float:
    return a * b


@pytest.mark.parametrize(
    ("sequence", "starting_value", "function", "right", "expected"),
    [
        ([1, 2, 3], 0, add, True, 6),
        ([0, 0, 0, 0], 5, add, True, 5),
        ([2, 2, 2, 2], 1, multiply, True, 16),
        ([1, 2, 3], 0, add, False, 6)
    ]
)
def test_valid_input(sequence, starting_value, function, right, expected):
    assert fold(sequence, starting_value, function, right) == expected


def test_empty_list():
    assert fold(sequence=[], starting_value=1, function=add) == 1


def test_no_list():
    with pytest.raises(TypeError):
        fold(sequence=1, starting_value=1, function=add)


def test_no_function():
    with pytest.raises(TypeError):
        fold(sequence=[1], starting_value=1, function="not callable")


def test_different_types():
    with pytest.raises(TypeError):
        fold(sequence=[1, 2], starting_value="wrong_type", function=add)
