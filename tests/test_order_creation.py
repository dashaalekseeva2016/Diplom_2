import allure
import pytest
from data import generate_random_user, TestData


class TestOrderCreation:
    @allure.title('Создание заказа с авторизацией')
    @allure.description('Проверка создания заказа авторизованным пользователем')
    def test_create_order_with_auth_success(self, registration_methods, order_methods):
        ingredients_response = order_methods.get_ingredients()
        ingredients_data = ingredients_response.json()
        
        assert ingredients_response.status_code == 200
        assert ingredients_data['success'] is True
       
        ingredient_id = ingredients_data['data'][0]['_id']
        
        user_data = generate_random_user()
        register_response = registration_methods.register_user(user_data)
        token = register_response.json().get('accessToken')
        
        ingredients = [ingredient_id]
        response = order_methods.create_order(ingredients, token)
        
        assert register_response.status_code == 200
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['success'] is True
        assert 'order' in response_data
        assert response_data['order']['number'] is not None

    @allure.title('Создание заказа без авторизации')
    @allure.description('Проверка создания заказа неавторизованным пользователем')
    def test_create_order_without_auth_success(self, order_methods):
        ingredients_response = order_methods.get_ingredients()
        ingredients_data = ingredients_response.json()
        
        assert ingredients_response.status_code == 200
        assert ingredients_data['success'] is True
        
        ingredient_id = ingredients_data['data'][0]['_id']
        
        ingredients = [ingredient_id]
        response = order_methods.create_order(ingredients)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['success'] is True
        assert 'order' in response_data
        assert response_data['order']['number'] is not None

    @allure.title('Создание заказа без ингредиентов')
    @allure.description('Проверка ошибки при создании заказа без ингредиентов')
    def test_create_order_without_ingredients_failed(self, order_methods):
        response = order_methods.create_order([])
        
        assert response.status_code == 400
        response_data = response.json()
        assert response_data['success'] is False

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    @allure.description('Проверка ошибки при неверном хеше ингредиента')
    def test_create_order_invalid_ingredient_hash_failed(self, order_methods):
        ingredients = [TestData.INVALID_INGREDIENT_HASH]
        response = order_methods.create_order(ingredients)
        
        assert response.status_code == 500
        