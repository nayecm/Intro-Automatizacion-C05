from selenium import webdriver

from source.core.selenium_actions import SeleniumActions


class LoginPage(SeleniumActions):
    input_user_name = "input[id='user-name']"
    input_password = "input[id=password]"
    button_submit = "input[id=login-button]"

    error_message = "h3[data-test=error]"

    def __init__(self, browser: webdriver):
        super().__init__(browser)

    def login(self, username, password):
        self.type_text(self.input_user_name, username)
        self.type_text(self.input_password, password)
        self.click(self.button_submit)