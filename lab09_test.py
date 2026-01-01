import numpy as np
from lab09 import replace_zeros

def test_replace_zero_basic():
    # zwykły przypadek: są zera, mają się zmienić na x
    A = [[0, 1, 0], [2, 0, 3]]
    result = replace_zeros(A, 3)
    assert result == [[3, 1, 3], [2, 3, 3]]

def test_replace_zero_no_zeros():
    # przypadek: brak zer, wynik powinien być taki sam
    A = [[1, 2], [3, 4]]
    result = replace_zeros(A, 9)
    assert result == [[1, 2], [3, 4]]

def test_replace_zeros_negative_value():
    # przypadek: zamiana na wartość ujemną
    A = [[0, 0], [5, 0]]
    result = replace_zeros(A, -7)
    assert result == [[-7, -7], [5, -7]]
