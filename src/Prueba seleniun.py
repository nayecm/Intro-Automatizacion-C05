import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_facebook_title():
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/?locale=es_LA')

    titulo_real = driver.title

    assert "Facebook" in titulo_real

    driver.quit()


def update_inputs():
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/?locale=es_LA')

    campo_email = driver.find_element(By.ID, "email")

    campo_email.send_keys("na")
    time.sleep(3)

    campo_email.send_keys("ye")
    time.sleep(3)

    campo_email.send_keys("@")
    time.sleep(3)

    campo_email.send_keys("gmail")
    time.sleep(3)

    campo_email.send_keys(".")
    time.sleep(3)

    campo_email.send_keys("com")
    time.sleep(3)

    driver.quit()

if __name__ == "__main__":
    # Llama solo a una función:
    update_inputs()
    # test_facebook_title()