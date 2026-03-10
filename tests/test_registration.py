import allure
import pytest
from data import generate_random_user, TestData


class TestUserRegistration:
    @allure.title('Успешная регистрация нового пользователя')
    @allure.description('Проверка, что нового пользователя можно зарегистрировать')
    def test_register_new_user_success(self, registration_methods):
        user_data = generate_random_user()
        
        response = registration_methods.register_user(user_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['success'] is True
        assert response_data['user']['email'] == user_data['email']
        assert response_data['user']['name'] == user_data['name']
        
    @allure.title('Ошибка при регистрации существующего пользователя')
    @allure.description('Проверка, что нельзя зарегистрировать уже существующего пользователя')
    def test_register_existing_user_failed(self, registration_methods):
        user_data = generate_random_user()
        create_response = registration_methods.register_user(user_data)
        
        response = registration_methods.register_user(user_data)
        
        assert create_response.status_code == 200
        assert response.status_code == 403
        response_data = response.json()
        assert response_data['success'] is False
    
    @allure.title('Ошибка при регистрации без обязательных полей')
    @allure.description('Проверка, что все обязательные поля должны быть заполнены')
    @pytest.mark.parametrize("user_data, expected_message", [
        (TestData.MISSING_EMAIL, "Email, password and name are required fields"),
        (TestData.MISSING_PASSWORD, "Email, password and name are required fields"),
        (TestData.MISSING_NAME, "Email, password and name are required fields")
    ])
    def test_register_missing_field_failed(self, registration_methods, user_data, expected_message):
        response = registration_methods.register_user(user_data)
        
        assert response.status_code == 403
        response_data = response.json()
        assert response_data['success'] is False
        