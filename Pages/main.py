from selenium import webdriver
from login import login_prod
from login import login_to_website
from selling_plan import create_selling_plan
from selling_plan import update_selling_plan
from selling_plan import add_selling_plan
from variants import create_variant
from categories import create_category


#************************************ MAIN *************************************************

def main():
    
    driver = webdriver.Chrome()
    try:
        login_prod(driver)
        create_category(driver)
        #create_variant(driver)
        #add_selling_plan(driver)
        #update_selling_plan(driver)
        #login_to_website(driver)
        #create_selling_plan(driver)
        
        #create_product(driver)
        
    finally:
        driver.quit()
   

if __name__ == "__main__":
    main()