

import pytest
from selenium.webdriver.common.by import By

from source.pages.LoginPage import LoginPage
from source.tests.base import BaseTest


class Test001(BaseTest):
    test_data = [{"username": "sss", "password": "aaa",
                  "expected": "Epic sadface: Username and password do not match any user in this service"},
                 {"username": "", "password": "secret_sauce", "expected": "Epic sadface: Username is required"},
                 {"username": "standard_user", "password": "", "expected": "Epic sadface: Password is required"}]

    @pytest.mark.parametrize("data", test_data)
    def test_open_browser_and_navigate(self, data, setup):

        login_page = LoginPage(self.browser)
        login_page.login(data["username"], data["password"])

        assert self.browser.find_element(By.CSS_SELECTOR, login_page.error_message).text == data["expected"]

    def test_login_success(self, setup):

        login_page = LoginPage(self.browser)
        login_page.login("standard_user", "secret_sauce")

        print("success")
    # assert driver.find_element(By.CSS_SELECTOR, login_page.error_message).text == data["expected"]
