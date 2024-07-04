from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest


#******************************* CREATE SELLING PLAN ********************************** 


def create_selling_plan(driver):

    wait = WebDriverWait(driver, 3)    
    
    # Seach gear button
    gear = driver.find_element(By.XPATH, "(//button[contains(@class, 'q-btn q-btn-item non-selectable no-outline logout_icon text-white q-btn--flat q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn--wrap q-btn--dense')])")
    gear.click()
    time.sleep(1)
    
    # Click on admin panel
    admin_panel = driver.find_element(By.XPATH, "(//span[contains(@class, 'font-700 cursor-pointer')])")
    time.sleep(1)
    admin_panel.click()
    time.sleep(1)
    
    # Click on selling plan button
    selling_plans_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'Body_F2 q-mb-none') and text()='Selling plans']")))
    selling_plans_button.click()
    time.sleep(1)
    
    # Click on add selling plan button
    add_selling_plan_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn q-btn-item non-selectable no-outline Button_F1 Button_S1 q-btn--standard q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn--wrap') ]")))
    add_selling_plan_button.click()
    time.sleep(1)
    
    # Fill input name
    input_name = driver.find_element(By.XPATH, "//input[contains(@class, 'q-field__native q-placeholder') ]")
    time.sleep(1)
    input_name.send_keys("New selling plan")
    time.sleep(2)
    ###############################################
    
    # DROPDOWN MENU ( solucionar dropdown)
    
    dropdown = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//i[@class='q-select__dropdown-icon q-icon notranslate material-icons']")))
    dropdown.click()
    time.sleep(1)
    # Expand dropdown
    type = driver.find_element(By.XPATH, "//div[contains(@class, 'q-field__native row items-center')]")
    span_element = type.find_element(By.TAG_NAME, 'span')
    
    # Assign value
    new_value = "Rent"
    driver.execute_script("arguments[0].innerText = arguments[1];", span_element, new_value)
    # Close dropdown
    dropdown.click()
    time.sleep(1)

    #############################################
    
    # Inputs Temporality
    inputs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
    )
    
    # Minimum Temporality
    inputs[6].send_keys("6")
    time.sleep(1)
    # Minimum Temporality Billing
    inputs[7].send_keys("0")
    time.sleep(1)
    # Period Price
    inputs[8].send_keys("11")
    time.sleep(1)
    # Taxes
    inputs[9].send_keys("21")
    time.sleep(5)



#*************************************** UPDATE SELLING PLAN ***************************************



def update_selling_plan(driver):
    
    wait = WebDriverWait(driver, 3) 
    # Seach gear button
    gear = driver.find_element(By.XPATH, "(//button[contains(@class, 'q-btn q-btn-item non-selectable no-outline logout_icon text-white q-btn--flat q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn--wrap q-btn--dense')])")
    gear.click()
    time.sleep(1)
    
    # Click on admin panel
    admin_panel = driver.find_element(By.XPATH, "(//span[contains(@class, 'font-700 cursor-pointer')])")
    time.sleep(1)
    admin_panel.click()
    time.sleep(1)
    
    # Click on selling plan button
    selling_plans_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'Body_F2 q-mb-none') and text()='Selling plans']")))
    selling_plans_button.click()
    time.sleep(3)

    #Click edit button
    button_edits = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
    )  
    button_edits[5].click()
    time.sleep(2)

    # Espera a que todos los botones estén presentes
    buttons = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
    )

    # Recorre todos los botones y obtiene su nombre y texto
    # for index, button in enumerate(buttons):
    #     name = button.get_attribute("name")
    #     text = button.text
    #     print(f"Botón {index + 1}:")
    #     print(f"  Nombre: {name}")
    #     print(f"  Texto: {text}")
    #     print("---------------------------------------------------")
    # Search las input before click add line
    inputs_edit = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
    )
    # for index, input_element in enumerate(inputs_edit):
    #     input_name = input_element.get_attribute("name")
    #     input_info = input_element.get_attribute("value")
    #     print(f"Posición: {index + 1}, Nombre: {input_name}, Info: {input_info}")
    
    # SCROLL DOWN 
    driver.execute_script("arguments[0].scrollIntoView(true);", inputs_edit[19])
    time.sleep(2)
    # Click on add line button
    buttons[11].click()
    time.sleep(2)

    inputs_edit = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
    )
    # for index, input_element in enumerate(inputs_edit):
    #     input_name = input_element.get_attribute("name")
    #     input_info = input_element.get_attribute("value")
    #     print(f"Posición: {index + 1}, Nombre: {input_name}, Info: {input_info}")

    inputs_edit[23].send_keys("24")
    time.sleep(1)
    inputs_edit[24].send_keys("0")
    time.sleep(1)
    inputs_edit[25].send_keys("5")
    time.sleep(1)
    inputs_edit[26].send_keys("21")

    time.sleep(2)

    buttons[14].click()
    time.sleep(5)

    # # SCROLL DOWN 
    # driver.execute_script("arguments[0].scrollIntoView(true);", inputs_edit[19])
    # time.sleep(5)

    


#************************************ MAIN *************************************************
