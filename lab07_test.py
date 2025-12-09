import pytest
import re
#funkcja z zadania 7
def validate_email(email):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    return bool(pattern.match(email))
def test_email_valid():
    assert validate_email("pyza181@gmail.com") == True
def test_email_no_at_sign():
    assert validate_email("pyza181gmail.com") == False
def test_email_invalid_chars():
    assert validate_email("pyza@gma!l.com") == False
#funkcja z zadania 4
def is_female_name_capitalized(name):
    return bool(re.fullmatch(r"[A-Z][a-z]*a", name))
def test_female_name_correct():
    assert is_female_name_capitalized("Anastazja") == True
def test_male_name():
    assert is_female_name_capitalized("Filip") == False
def test_lowercase_name():
    assert is_female_name_capitalized("anastazja") == False