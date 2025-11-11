from lab06 import coding

def test_encrypt_decrypt():
    text = "algorytm"
    key = "kod"
    encrypted = coding(text, key)
    decrypted = coding(encrypted, key)
    assert decrypted == text

def test_different_texts_produce_different_encryptions():
    key = "abc"
    encrypted1 = coding("hello", key)
    encrypted2 = coding("world", key)
    assert encrypted1 != encrypted2

def test_same_text_produce_different_keys():
    text = "test"
    encrypted1 = coding(text, "key1")
    encrypted2 = coding(text, "key2")
    assert encrypted1 != encrypted2
s