from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest

#****************************** LOGIN DEVELOPMENT ***********************************

def login_to_website(driver):
    
    
    wait = WebDriverWait(driver, 10)

    try:
        #driver = webdriver.Chrome()
        driver.get('https://app.dev.gosharpei.com/')
        time.sleep(1)
        # SEARCH ELEMENT
        input_email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        input_password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        login_button = driver.find_element(By.CSS_SELECTOR, "button")
        
        # SEND KEYS
        input_email.send_keys("demo@gosharpei.com")
        time.sleep(1)
        input_password.send_keys("Sharpei2023@")
        time.sleep(1)
        
        # CLICK LOGIN BUTTON
        login_button.click()
        time.sleep(4)

        # FIND BUTTONS
        buttons = driver.find_elements(By.CSS_SELECTOR, "button")
        print(len(buttons))
        time.sleep(4)
    
        starter_button = buttons[2]
        print(starter_button.accessible_name)
        print()
        print("-----------------------------------------------------------")
        
        # SCROLL DOWN 
        driver.execute_script("arguments[0].scrollIntoView(true);", starter_button)
        time.sleep(5)
        
        # CLICK
        starter_button.click()
        time.sleep(3)


        div_element = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CLASS_NAME, '__PrivateStripeElement')))
        print(div_element.get_dom_attribute("class"))
        
        
        # Search Iframe
        iframe = div_element.find_element(By.TAG_NAME, 'iframe')
        print(iframe.get_dom_attribute("title"))
        
        # Switch context
        driver.switch_to.frame(iframe)
        print("Switched to iframe")

         # Search elements in input
        input_elements = driver.find_elements(By.TAG_NAME, 'input')
         # Print attributes
        for input_element in input_elements:
            input_id = input_element.get_attribute("id")
            
            if input_id == "Field-numberInput":
                input_element.send_keys("4242424242424242")  
                time.sleep(1)
            elif input_id == "Field-expiryInput":
                input_element.send_keys("1230")  
                time.sleep(1)
            elif input_id == "Field-cvcInput":
                input_element.send_keys("123")  
                time.sleep(1)
            
        time.sleep(3)

        driver.switch_to.default_content()
        print("Switched to default content")
        time.sleep(1)
        print("--------comienza default content -------")

        # Search element by id
        boton_pagar = driver.find_element(By.ID, "submit")
        #print(boton_pagar.get_dom_attribute("class"))
        time.sleep(1)
        boton_pagar.click()
        time.sleep(2)
        
        # Search submit button
        boton_get_started = driver.find_element(By.CSS_SELECTOR, "button")
        time.sleep(4)
        
        driver.execute_script("arguments[0].scrollIntoView(true);", boton_get_started)
        time.sleep(4)
        boton_get_started.click()
        time.sleep(4)


    finally:
        time.sleep(2)


#********************************** LOGIN PROD ***********************************

def login_prod(driver):
    
        driver.get('https://app.prod.gosharpei.com/')
        time.sleep(1)
        # SEARCH ELEMENT
        input_email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        input_password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        login_button = driver.find_element(By.CSS_SELECTOR, "button")
        
        # SEND KEYS
        input_email.send_keys("josebrest25@gmail.com")
        #time.sleep(1)
        input_password.send_keys("Sharpei2023@")
        #time.sleep(1)
        
        # CLICK LOGIN BUTTON
        login_button.click()
        time.sleep(5)

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

def main():
    
    driver = webdriver.Chrome()
    try:
        login_prod(driver)
        update_selling_plan(driver)
        #login_to_website(driver)
        #create_selling_plan(driver)
        
        #create_product(driver)
        
    finally:
        driver.quit()
   

if __name__ == "__main__":
    main()
