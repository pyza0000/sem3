import pytest
from lab06 import coding

def test_coding_encrypt_decrypt():#sprawdzam czy szyfrowanie i odszyfrowanie działa dobrze
    word = "algorytm"
    key = "kodykody"
    encrypted = coding(word, key)
    decrypted = coding(encrypted, key)
    assert decrypted == word

def test_coding_different_keys(): #Testuje, że różne klucze dają różne wyniki
    word = "jaciechyca"
    key1 = "abcdefghij"
    key2 = "1234567890"
    encrypted1 = coding(word, key1)
    encrypted2 = coding(word, key2)
    assert encrypted1 != encrypted2

def test_coding_empty_string(): #Testuje przypadek pustego napisu
    word = ""
    key = ""
    result = coding(word, key)
    assert result == ""
