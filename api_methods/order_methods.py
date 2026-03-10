import requests
import allure
from urls import Urls


class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(ingredients, token=None):
        headers = {}
        if token:
            headers['Authorization'] = token
        
        payload = {"ingredients": ingredients}
        return requests.post(Urls.CREATE_ORDER, json=payload, headers=headers)

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_ingredients():
        return requests.get(Urls.INGREDIENTS)