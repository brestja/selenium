from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest

def create_category(driver):
    wait = WebDriverWait(driver, 3) 
    # Seach gear button
    gear = driver.find_element(By.XPATH, "(//button[contains(@class, 'q-btn q-btn-item non-selectable no-outline logout_icon text-white q-btn--flat q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn--wrap q-btn--dense')])")
    gear.click()
    time.sleep(1)
    
    # Click on admin panel
    admin_panel = driver.find_element(By.XPATH, "(//span[contains(@class, 'font-700 cursor-pointer')])")
    time.sleep(1)
    admin_panel.click()
    time.sleep(5)

    # Click on categories button
    categories_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'Body_F2 q-mb-none') and text()='Categories']")))
    categories_button.click()
    time.sleep(8)

    # Click on add category button
    add_category_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn q-btn-item non-selectable no-outline Button_F1 Button_S1 q-btn--flat q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn--wrap') ]")))
    add_category_button.click()
    time.sleep(7)

    # Input category name
    input_category_name = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[contains(@class, 'q-field__native q-placeholder') ]")))
    input_category_name.send_keys("New category")
    time.sleep(7)

    # Creat new category button
    save_category_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn q-btn-item non-selectable no-outline Button_F1 Button_S1 HalfWidthButton q-btn--flat q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn--wrap') ]")))
    save_category_button.click()
    time.sleep(7)


    


   