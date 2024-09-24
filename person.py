"""Person example."""
from dataclasses import dataclass
from cs110 import expect, summarize

@dataclass
class Person:
    """A class to describe a person."""
    name: str
    age: int
    
def birth_year(p: Person, year: int) -> int:
    """
    Purpose: Gets the birth year of a person given the current year.
    Examples: 
        birth_year(Person("Paul", 38), 2024) -> 2024 - 38 == 1986
        birth_year(Person("James", 12), 2024) -> 2024 - 12 == 2012
    """
    return year - p.age
    
expect(birth_year(Person("Paul",  38), 2024), equals = 2024 - 38)
expect(birth_year(Person("James", 12), 2024), equals = 2024 - 12)


def older(p1: Person, p2: Person) -> Person:
    """
    Purpose: Returns the older of two people.
    Examples:
        a = Person("Alex", 12)
        b = Person("Bob", 23)
        c = Person("Charlie", 42)
        older(a, b) -> b
        older(b, c) -> c
        older(a, c) -> c
    """
    if p1.age > p2.age:
        return p1
    else:
        return p2

a = Person("Alex", 12)
b = Person("Bob", 23)
c = Person("Charlie", 42)
expect(older(a, b), equals = b)
expect(older(b, c), equals = c)
expect(older(a, c), equals = c)

summarize()
