import pytest
from lab04 import Student

def test_equal_students():
    s1 = Student()
    s1.give_name("Anna", "Nowak")
    s1.give_mark(5)
    s1.give_mark(4)

    s2 = Student()
    s2.give_name("Jan", "Kowalski")
    s2.give_mark(5)
    s2.give_mark(4)

    assert s1 == s2


def test_different_students():
    s1 = Student()
    s1.give_name("Anna", "Nowak")
    s1.give_mark(5)
    s1.give_mark(4)

    s2 = Student()
    s2.give_name("Jan", "Kowalski")
    s2.give_mark(3)
    s2.give_mark(4)

    assert s1 > s2


def test_less_than():
    s1 = Student()
    s1.give_name("Anna", "Nowak")
    s1.give_mark(3)
    s1.give_mark(3)

    s2 = Student()
    s2.give_name("Jan", "Kowalski")
    s2.give_mark(5)
    s2.give_mark(4)

    assert s1 < s2

