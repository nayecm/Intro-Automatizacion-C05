# Trabajo final

# Utilizando el proyecto de codigo, que se ha empleado para los laboratorios:
#  1. Crear un test case end to end, que siga el siguiente flujo paso a paso.
#x  	1.1 Iniciar sesion en la app https://www.saucedemo.com/v1/
#x  	1.2 Agregar 2 elementos al carrito, haciendo click en el boton "Add to Cart" para cada uno.
#x  	1.3 Navegar al carrito, haciendo click en el icono que aparece en la esquina superior derecho.
#x  	1.4 Verificar que se hayan agregado ambos items y hacer click al boton "checkout" (validar que el color del boton sea el correcto)
#x  	1.5 Llenar el formulario intermedio con la direccion y hacer click en el boton "continue"
#x  	1.6 Verificar el que la cantidad total sea la suma de los 2 articulos mas el tax.
# 	1.7 Hacer click en el boton "finishi" y validar que el mensaje de que la orden se ha enviado.
# 	1.8 Hacer click en el menu de la esquina superior izquierda y desloguearse de la aplicacion.
# 	1.9 Verificar que el usuario se deslogueo correctamente.

# 2. Se debera presentar un doc, pdf o excel con el caso de prueba, dicho caso de prueba debe contener cada paso y resultado esperado.
# 3. Se espera que el test case automatizado cumpla las normas vistas en clase y sea una representacion fiel del caso de prueba manual.
# 4. Puede usar page object model o keyword driven

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_caso1():
    opciones = webdriver.ChromeOptions()

    opciones.add_argument("--incognito")

    driver = webdriver.Chrome(options=opciones)

    driver.get("https://www.saucedemo.com/v1/index.html")

    input_user_name = driver.find_element(By.ID, "user-name")

    input_password = driver.find_element(By.ID, "password")

    boton_login = driver.find_element(By.ID, "login-button")

    input_user_name.send_keys("standard_user")
    time.sleep(0.5)

    input_password.send_keys("secret_sauce")
    time.sleep(0.5)

    boton_login.click()
    time.sleep(1)

    # assert "https://www.saucedemo.com/v1/inventory.html" == driver.current_url

    # Localizar todos los botones de "ADD TO CART" visibles
    botones_add = driver.find_elements(By.CSS_SELECTOR, ".btn_inventory")

    # Hacer clic en los dos primeros botones
    for boton in botones_add[:2]:  # Solo los dos primeros
        boton.click()
        time.sleep(0.5)  # Pequeña pausa para que el click se procese

    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container a").click()

    time.sleep(1)

    cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")

    assert len(cart_items) == 2

    boton_checkout = driver.find_element(By.CLASS_NAME, "checkout_button")

    color_css = boton_checkout.value_of_css_property("background-color")

    print("Color CSS:", color_css)

    assert color_css == "rgba(226, 35, 26, 1)"; # rojo
    time.sleep(0.5)

    boton_checkout.click()
    time.sleep(0.5)

    input_first_name = driver.find_element(By.ID, "first-name")

    input_last_name = driver.find_element(By.ID, "last-name")

    input_postal_code = driver.find_element(By.ID, "postal-code")

    boton_continuar = driver.find_element(By.CSS_SELECTOR, ".checkout_buttons .cart_button")

    input_first_name.send_keys("Nayeli")
    time.sleep(0.5)

    input_last_name.send_keys("Castillo")
    time.sleep(0.5)

    input_postal_code.send_keys("30106")
    time.sleep(0.5)

    boton_continuar.click()
    time.sleep(1)

    subtotal_text = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    tax_text = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
    total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    # Extraer valores numéricos
    subtotal = float(subtotal_text.replace("Item total: $", ""))
    tax = float(tax_text.replace("Tax: $", ""))
    total = float(total_text.replace("Total: $", ""))

    # Validar la suma
    if round(subtotal + tax, 2) == total:
        print("✅ El total es correcto")
    else:
        print(f"❌ El total es incorrecto. Esperado {subtotal + tax}, encontrado {total}")

    assert round(subtotal + tax, 2) == total

    time.sleep(3)
    driver.quit()

