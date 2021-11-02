import pytest

from solution.src.fold import fold


ADD = (lambda a, b: a + b)
MULTIPLY = (lambda a, b: a * b)


@pytest.mark.parametrize(
    ("sequence", "starting_value", "function", "right", "expected"),
    [
        ([1, 2, 3], 0, ADD, True, 6),
        ([0, 0, 0, 0], 5, ADD, True, 5),
        ([2, 2, 2, 2], 1, MULTIPLY, True, 16),
        ([1, 2, 3], 0, ADD, True, 6)
    ]
)
def test_fold_valid_input(sequence, starting_value, function, right, expected):
    assert fold(sequence, starting_value, function, right) == expected


def test_fold_no_list():
    with pytest.raises(Exception):
        fold(1, 1, ADD)


def test_fold_no_function():
    with pytest.raises(Exception):
        fold([1], 1, 1)


def test_fold_different_types():
    with pytest.raises(Exception):
        fold([1, 2], "3", 6)
