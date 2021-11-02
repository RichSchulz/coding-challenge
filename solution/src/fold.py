from typing import Callable, List, TypeVar


A = TypeVar('A')
B = TypeVar('B')


# TODO: Check if types match, maybe add class for function & custom exception
def fold(sequence: List[A],
         starting_value: B,
         function: Callable[[A, B], B],
         right: bool = True) -> B:
    """Custom implementation of the higher order function fold
    Parameters:
        sequence (List): The sequence to be folded
        starting_value (T): The starting value of the folding
        function (Callable): The function to be used for folding
        right (bool): If true a right fold is performed, else a left fold
    Returns:
        T: The result of the folding"""
    # If a left fold should be performed
    # the computation order has to be changed by reversing the sequence.
    if not right:
        sequence.reverse()

    for value in sequence:
        starting_value = function(starting_value, value)

    return starting_value
