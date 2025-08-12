import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_caso1():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/v1/index.html")

    input_user_name = driver.find_element(By.ID, "user-name")

    input_password = driver.find_element(By.ID, "password")

    boton_login = driver.find_element(By.ID, "login-button")

    input_user_name.send_keys("standard_user")
    time.sleep(3)

    input_password.send_keys("secret_sauce")
    time.sleep(3)

    boton_login.click()
    time.sleep(3)

    assert "https://www.saucedemo.com/v1/inventory.html" == driver.current_url

    driver.quit()

def test_caso2():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/v1/index.html")

    input_user_name = driver.find_element(By.ID, "user-name")

    input_password = driver.find_element(By.ID, "password")

    boton_login = driver.find_element(By.ID, "login-button")

    input_user_name.send_keys("problem_user")
    time.sleep(3)

    input_password.send_keys("problem_user")
    time.sleep(3)

    boton_login.click()
    time.sleep(3)

    error_element = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
    mensaje_error = error_element.text

    assert "Epic sadface: Username and password do not match any user in this service" == mensaje_error

    driver.quit()

def test_caso3():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/v1/index.html")

    input_user_name = driver.find_element(By.ID, "user-name")

    input_password = driver.find_element(By.ID, "password")

    boton_login = driver.find_element(By.ID, "login-button")

    input_user_name.send_keys("standard_use")
    time.sleep(3)

    input_password.send_keys("")
    time.sleep(3)

    boton_login.click()
    time.sleep(3)

    error_element = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
    mensaje_error = error_element.text

    assert "Epic sadface: Password is required" == mensaje_error

    driver.quit()