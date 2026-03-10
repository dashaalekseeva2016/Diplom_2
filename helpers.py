import random
import string
import requests
from urls import Url


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


def get_ingredients():
    response = requests.get(Url.INGREDIENTS)
    if response.status_code == 200:
        data = response.json()
        if data.get('success') and data.get('data'):
            return [ingredient['_id'] for ingredient in data['data']]
    return []


def register_user(user_data):
    return requests.post(Url.CREATE_USER, json=user_data)


def login_user(credentials):
    return requests.post(Url.LOGIN_USER, json=credentials)


def create_order(ingredients, token=None):
    headers = {}
    if token:
        headers['Authorization'] = token
    
    payload = {"ingredients": ingredients}
    return requests.post(Url.CREATE_ORDER, json=payload, headers=headers)


def delete_user(token):
    headers = {'Authorization': token}
    return requests.delete(Url.BASE_URL + '/auth/user', headers=headers)