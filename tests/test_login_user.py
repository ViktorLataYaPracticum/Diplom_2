import allure
from helpers import generate_user, create_user, login_user
from data.payload_data import WRONG_LOGIN,WRONG_PASSWORD
from data.expected_data import *

@allure.suite("Тесты авторизации пользователя")
class TestLoginUser:
    @allure.title("Логин существующего пользователя")
    def test_login_existing_user(self,new_user):
        user, _ = new_user

        response = login_user(
            user["email"],
            user["password"]
        )

        assert response.status_code == ExpectedResponceCodes.LOGIN_SUCCESS
        assert response.json()["success"] is True


    @allure.title("Логин с неверным логином и паролем")
    def test_login_wrong_credentials(self):
        response = login_user(
            WRONG_LOGIN,
            WRONG_PASSWORD
        )

        assert response.status_code == ExpectedResponceCodes.LOGIN_WRONG_AUTORIZATION_DATA
        assert response.json()["success"] is False
        assert response.json()["message"] == ExpectedResponces.LOGIN_WRONG_AUTORIZATION_DATA

    @allure.title("Логин существующего пользователя с пустым паролем")
    def test_login_existing_user_without_password(self,new_user):
        user, _ = new_user

        response = login_user(
            user["email"],""
            
        )

        assert response.status_code == ExpectedResponceCodes.LOGIN_WITHOUT_ANY_FIELD
        assert response.json()["success"] is False
        assert response.json()["message"] == ExpectedResponces.LOGIN_WITHOUT_ANY_FIELD

    @allure.title("Логин существующего пользователя с пустым логином")
    def test_login_existing_user_without_login(self,new_user):
        user, _ = new_user

        response = login_user(
            "",user["password"]
        )

        assert response.status_code == ExpectedResponceCodes.LOGIN_WITHOUT_ANY_FIELD
        assert response.json()["success"] is False
        assert response.json()["message"] == ExpectedResponces.LOGIN_WITHOUT_ANY_FIELD

    @allure.title("Логин существующего пользователя с неверным паролем")
    def test_login_existing_user_with_wrong_password(self,new_user):
        user, _ = new_user

        response = login_user(
            user["email"],WRONG_PASSWORD
            
        )

        assert response.status_code == ExpectedResponceCodes.LOGIN_WRONG_AUTORIZATION_DATA
        assert response.json()["success"] is False
        assert response.json()["message"] == ExpectedResponces.LOGIN_WRONG_AUTORIZATION_DATA
