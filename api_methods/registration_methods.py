import requests
import allure
from urls import Urls


class RegistrationMethods:
    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def register_user(user_data):
        return requests.post(Urls.CREATE_USER, json=user_data)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        headers = {'Authorization': token}
        return requests.delete(Urls.USER_INFO, headers=headers)