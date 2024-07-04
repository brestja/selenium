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














