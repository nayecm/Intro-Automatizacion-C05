from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:
    browser_name = None

    def __init__(self, browser_name: str):
        self.browser_name = browser_name

    def get_instance(self):
        if self.browser_name == "CHROME":
            pref = {"profile.password_manager_leak_detection": False}
            chrome_options = Options()
            chrome_options.add_experimental_option("prefs", pref)
            return webdriver.Chrome(options=chrome_options)
        if self.browser_name == "FIREFOX":
            return webdriver.Firefox()
        else:
            return None
