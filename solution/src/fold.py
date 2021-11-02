from typing import Callable, List


# TODO: Check if types match, maybe add class for function & custom exception
def fold(sequence: List[any],
         starting_value: any,
         function: Callable[[any, any], any]):
    for value in sequence:
        starting_value = function(starting_value, value)
    return starting_value
