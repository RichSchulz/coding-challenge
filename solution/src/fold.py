from typing import Callable, List, TypeVar


A = TypeVar('A')
B = TypeVar('B')


# TODO: Check if types match, maybe add class for function & custom exception
def fold(sequence: List[A],
         starting_value: B,
         function: Callable[[A, B], B],
         right: bool = True) -> B:
    """Custom implementation of the higher order function fold"""
    # If a left fold should be performed
    # the computation order has to be changed by reversing the sequence.
    if not right:
        sequence.reverse()

    for value in sequence:
        starting_value = function(starting_value, value)

    return starting_value
