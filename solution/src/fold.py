from typing import Callable, List, TypeVar


A = TypeVar('A')
B = TypeVar('B')


# TODO: Check if types match, maybe add class for function & custom exception
def fold(sequence: List[A],
         starting_value: B,
         function: Callable[[A, B], B]) -> B:
    """Custom implementation of the higher order function fold"""
    for value in sequence:
        starting_value = function(starting_value, value)
    return starting_value
