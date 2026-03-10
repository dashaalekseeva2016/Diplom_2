import pytest
from api_methods.registration_methods import RegistrationMethods
from api_methods.login_methods import LoginMethods
from api_methods.order_methods import OrderMethods
from data import generate_random_user


@pytest.fixture
def registration_methods():
    return RegistrationMethods()


@pytest.fixture
def login_methods():
    return LoginMethods()


@pytest.fixture
def order_methods():
    return OrderMethods()


@pytest.fixture
def create_and_delete_user(registration_methods):
    user_data = generate_random_user()
    response = registration_methods.register_user(user_data)
    
    user_info = {
        "data": user_data,
        "response": response
    }
    
    if response.status_code == 200:
        response_json = response.json()
        user_info["token"] = response_json.get('accessToken')
        user_info["refresh_token"] = response_json.get('refreshToken')
    
    yield user_info
    
    if user_info.get("token"):
        registration_methods.delete_user(user_info["token"])


@pytest.fixture
def ingredients_list(order_methods):
    response = order_methods.get_ingredients()
    if response.status_code == 200:
        data = response.json()
        if data.get('success') and data.get('data'):
            return [ingredient['_id'] for ingredient in data['data']]
    return []