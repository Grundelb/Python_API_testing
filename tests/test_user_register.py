import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    def test_user_with_existing_email(self):
        url = "https://playground.learnqa.ru/api/user/"
        email = "vinkotov@example.com"
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post(url, data= data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpexted response content {response.content}"