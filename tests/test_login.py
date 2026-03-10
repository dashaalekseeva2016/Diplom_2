import allure
import pytest
from data import generate_random_user, TestData


class TestUserLogin:
    @allure.title('Успешный вход существующего пользователя')
    @allure.description('Проверка, что зарегистрированный пользователь может войти')
    def test_login_existing_user_success(self, registration_methods, login_methods):
        user_data = generate_random_user()
        register_response = registration_methods.register_user(user_data)
        
        login_data = {
            "email": user_data['email'],
            "password": user_data['password']
        }
        login_response = login_methods.login_user(login_data)
        
        assert register_response.status_code == 200
        assert login_response.status_code == 200
        response_data = login_response.json()
        assert response_data['success'] is True
        
    @allure.title('Ошибка входа с неверными учетными данными')
    @allure.description('Проверка, что нельзя войти с неверным email и паролем')
    def test_login_invalid_credentials_failed(self, login_methods):
        response = login_methods.login_user(TestData.INVALID_LOGIN)
        
        assert response.status_code == 401

    @allure.title('Ошибка входа с неверным паролем для существующего пользователя')
    @allure.description('Проверка, что нельзя войти с неверным паролем')
    def test_login_invalid_password_failed(self, registration_methods, login_methods):
        user_data = generate_random_user()
        register_response = registration_methods.register_user(user_data)
        
        login_data = {
            "email": user_data['email'],
            "password": "wrongpassword"
        }
        login_response = login_methods.login_user(login_data)
        
        assert register_response.status_code == 200
        assert login_response.status_code == 401
        response_data = login_response.json()
        assert response_data['success'] is False
        
