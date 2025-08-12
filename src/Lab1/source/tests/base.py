import pytest

from source.core.browser import Browser


class BaseTest:
    browser = None

    @pytest.fixture
    def setup(self):
        self.browser = Browser("CHROME").get_instance()
        self.browser.get("https://www.saucedemo.com/v1/")
