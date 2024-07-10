from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest



def create_variant(driver):
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
    
    # Click on Variants button
    variants_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'Body_F2 q-mb-none') and text()='Variants']")))
    variants_button.click()
    time.sleep(6)

    # Click on add selling plan button
    add_variant_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn q-btn-item non-selectable no-outline Button_F1 Button_S1 q-btn--standard q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn--wrap') ]")))
    add_variant_button.click()
    time.sleep(7)

    # Input variant name
    input_variant_name = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[contains(@class, 'q-field__native q-placeholder') ]")))
    input_variant_name.send_keys("New variant")
    time.sleep(7)

    # Save new variant 
    save_variant_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'q-btn q-btn-item non-selectable no-outline Button_F1 Button_S1 q-btn--flat q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn--wrap') ]")))
    save_variant_button.click()
    time.sleep(7)


   

    