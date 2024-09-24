"""Iterable examples."""
from typing import List, Set, Tuple, Dict, Any
from cs110 import expect, summarize

my_int_list  = [1, 2, 3]
my_str_list  = ["a", "b", "c"]
my_bool_list = [True, False, False]

# Accessing 0-indexed
print(my_int_list[0])
print(my_str_list[1])
print(my_bool_list[2])

# Accessing from back of list
print(my_int_list[-1])
print(my_str_list[-2])
print(my_bool_list[-3])

# Accessing ranges
print(my_int_list[0:])
print(my_str_list[1:3])
print(my_bool_list[:2])

# For-loop
for i in my_int_list:
    print(i)



def add(lon: List[float | int]) -> float | int:
    """
    Purpose: Adds a list of numbers.
    Examples: 
        add([1, 2, 3]) -> 1 + 2 + 3 == 6
        add([]) -> 0
    """
    # acc stores the accumulated result
    acc: float = 0
    for n in lon:
        acc = acc + n
    return acc

expect(add([]), equals = 0)
expect(add([1, 2, 3]), equals = 1 + 2 + 3)


def average(lon: List[float | int]) -> float | None:
    """
    Purpose: Adds a list of numbers.
    Examples: 
        average([1, 2, 3]) -> (1 + 2 + 3) / 3 == 2
        average([]) -> None
    """
    # acc stores the accumulated result
    if len(lon) == 0:
        return None
    acc: float = 0
    for n in lon:
        acc = acc + n
    return acc / len(lon)

expect(average([]), None) # Don't want to divide by zero
expect(average([1, 2, 3]), equals = (1 + 2 + 3) / 3)

def multiply(lon: List[int]) -> int | None:
    """
    Purpose: Adds a list of numbers.
    Examples: 
        multiply([1, 2, 3]) -> 1 * 2 * 3 == 6
        multiply([1, 0, 3]) -> 1 * 0 * 3 == 0
        multiply([]) -> None
    """
    # acc stores the accumulated result
    if len(lon) == 0:
        return None
    acc = 1
    for n in lon:
        acc = acc * n
    return acc

expect(multiply([]), None) # Doesn't make sense for none.
expect(multiply([1, 2, 3]), equals = 1 * 2 * 3)
expect(multiply([1, 0, 3]), equals = 1 * 0 * 3)

def most(t: Tuple[Any, ...]) -> int:
    """
    Purpose: Returns the count of the most frequent element in a tuple.
    Examples: 
        most((1, 2, 3)) -> 1
        most((1, 1, 2)) -> 2
        most((1, 1, 1, 2, 2)) -> 3
        
    """
    highest = 0
    for element in t:
        if t.count(element) > highest:
            highest = t.count(element)
    return highest

expect(most((1, 2, 3)), equals = 1)
expect(most((1, 1, 2)), equals = 2)
expect(most((1, 1, 1, 2, 2)), equals = 3)


def contains(s: Set[Any], element: Any) -> bool:
    """
    Purpose: Checks whether an element is in a set.
    Examples: 
        contains({1,2,3}, 1) -> True
        contains({1,2,3}, 0) -> False
        contains({"a","b","c"}, "a") -> True
        contains({"a","b","c"}, "d") -> False
    """
    for member in s:
        if member == element:
            return True
    return False

expect(contains({1,2,3}, 1), equals = True)
expect(contains({1,2,3}, 0), equals = False)
expect(contains({"a","b","c"}, "a"), equals = True)
expect(contains({"a","b","c"}, "d"), equals = False)


def dictionary_average(d: Dict[str, float | int]) -> float | None:
    """
    Purpose: Averages the values of a dictionary.
    Examples: 
        dictionary_average({}) -> None
        dictionary_average({"a": 1}) -> 1
        dictionary_average({"a": 1, "b": 2}) -> 1.5
        dictionary_average({"a": 1, "b": 2, "c": 3}) -> 2
    """
    if len(d) == 0:
        return None
    acc: float = 0
    for key in d:
        acc = acc + d[key]
    return acc / len(d)

expect(dictionary_average({}), None)
expect(dictionary_average({"a": 1}), equals = 1)
expect(dictionary_average({"a": 1, "b": 2}), equals = 1.5)
expect(dictionary_average({"a": 1, "b": 2, "c": 3}), equals = 2)

summarize()