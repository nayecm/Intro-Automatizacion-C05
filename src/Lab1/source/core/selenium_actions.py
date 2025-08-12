from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumActions:
    browser: webdriver

    def __init__(self, browser):
        self.browser = browser

    def click(self, element: str):
        element = self.wait_until_element_clickable(element)
        element.click()

    def type_text(self, element: str, text: str):
        element = self.wait_until_element_clickable(element)
        element.send_keys(text)

    def wait_until_element_clickable(self, locator):
        element = self.browser.find_element(By.CSS_SELECTOR, locator)
        wait = WebDriverWait(self.browser, timeout=30, poll_frequency=.2, ignored_exceptions=[NoSuchElementException, ElementNotInteractableException])
        return wait.until(expected_conditions.element_to_be_clickable(element))