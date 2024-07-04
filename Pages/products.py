from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest

#************************************** CREATE PRODUCT ********************************************

def create_product(driver):
    
    driver.get('https://app.dev.gosharpei.com/admin/dashboard')
    time.sleep(2)

    # Search all buttons
    buttons_inv = driver.find_element(By.XPATH, "(//button[contains(@class, 'q-btn q-btn-item non-selectable no-outline q-btn--standard q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn--wrap dropbtn')])[2]")
    
    # Hover button
    ActionChains(driver).move_to_element(buttons_inv).perform()
    time.sleep(2)

    product_button = driver.find_element(By.XPATH, "//a[contains(@href, '/admin/products')]")
    product_button.click()
    time.sleep(5)
    
    # Click add product button
    add_product_button = driver.find_element(By.XPATH, "(//button[contains(@class, 'q-btn q-btn-item non-selectable no-outline Button_F1 Button_S1 q-btn--flat q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn--wrap')])")
    time.sleep(4)
    add_product_button.click()
    time.sleep(6)

    # Add product name
    input_name_product = driver.find_element(By.XPATH, "(//input[contains(@placeholder, 'Enter the name')])")
    time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView(true);", input_name_product)
    time.sleep(2)
    input_name_product.send_keys("test product selenium")
    time.sleep(1)
    
    # Add remote id
    input_remote_id = driver.find_element(By.XPATH, "(//input[contains(@placeholder, 'Enter remote id')])")
    time.sleep(1)
    input_remote_id.send_keys("123568980")
    time.sleep(5)

    # Add description
    description = driver.find_element(By.XPATH, "(//div[contains(@class, 'q-editor__content')])")
    description.send_keys("test product selenium 1")
    time.sleep(5)

    save_button = driver.find_elements(By.CSS_SELECTOR, "button")

    for button in save_button:
        if button.text == "Save":
            
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            WebDriverWait(driver, 10).until(EC.visibility_of(button))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button))
            # Click save button
            button.click()
            break  
    
    time.sleep(5)