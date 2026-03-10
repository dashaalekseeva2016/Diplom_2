import random
import string


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_email():
    return f"{generate_random_string(8)}@test.com"


def generate_random_user():
    return {
        "email": generate_random_email(),
        "password": generate_random_string(10),
        "name": generate_random_string(8)
    }


class TestData:
    
    MISSING_EMAIL = {
        "password": "password123",
        "name": "TestUser"
    }
    
    MISSING_PASSWORD = {
        "email": "test@example.com",
        "name": "TestUser"
    }
    
    MISSING_NAME = {
        "email": "test@example.com",
        "password": "password123"
    }

    INVALID_LOGIN = {
        "email": "wrong@example.com",
        "password": "wrongpass"
    }
    
    INVALID_INGREDIENT_HASH = "invalid_hash_123"