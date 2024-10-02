import string
import pytest
from FinalProject import shuffle_characters, generate_strong_password

def test_shuffle_characters():
    """Verify that the shuffle_characters function shuffles characters correctly."""
    password = "password123"
    shuffled_password = shuffle_characters(password)
    
    assert password != shuffled_password
    
    assert len(password) == len(shuffled_password)
    
    for char in password:
        assert char in shuffled_password


def test_generate_strong_password():
    """Verify that the generate_strong_password function generates a strong password."""
    password_length = 12
    generated_password = generate_strong_password(password_length)
    assert len(generated_password) == password_length

    has_uppercase = any(char.isupper() for char in generated_password)
    has_lowercase = any(char.islower() for char in generated_password)
    has_digit = any(char.isdigit() for char in generated_password)
    has_punctuation = any(char in string.punctuation for char in generated_password)

    assert has_uppercase
    assert has_lowercase
    assert has_digit
    assert has_punctuation

pytest.main(["-v", "--tb=line", "-rN", __file__])






