import requests
import allure
from urls import Urls


class LoginMethods:
    @staticmethod
    @allure.step("Вход пользователя")
    def login_user(credentials):
        return requests.post(Urls.LOGIN_USER, json=credentials)