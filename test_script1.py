from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()
user_matrix = [["carlosmiguel.villanueva27@gmail.com", "L&GAnnex100%", "lgAnnex100%"]]

browser.implicitly_wait(30)
browser.maximize_window()
browser.get("https://www.linkedin.com/")
hraw_html = browser.page_source



def homepage_autentication():

        
    def homepage_authentication__successful():
        try:
            username_field = browser.find_element(By.NAME, 'session_key')
            password_field = browser.find_element(By.NAME, 'session_password')
            submit_button = browser.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn' and @type='submit']")
        finally:
            print("Changes detected as selectors do not detect previous indicators")
            try:
                username_field = browser.find_element(By.NAME, 'session_key')
                password_field = browser.find_element(By.NAME, 'session_password')
                submit_button = browser.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn' and @type='submit']")
                
            finally:
                print("no fields were found")
        username_field.send_keys(user_matrix[0][0])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        password_field.send_keys(user_matrix[0][1])
        submit_button.click() 

    def homepage_authentication__unsuccessful():
        username_field = browser.find_element(By.NAME, 'session_key')
        password_field = browser.find_element(By.NAME, 'session_password')
        submit_button = browser.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn' and @type='submit']")
        username_field.send_keys(user_matrix[0][0])
        password_field.send_keys(user_matrix[0][2])
        submit_button.click()
        
    #authenticate succesfully or not based in random value
    # auth_random = random.randint(1,2)
    auth_random = 2
    if auth_random == 1:
        homepage_authentication__successful()
    else:
        homepage_authentication__unsuccessful()
        homepage_authentication__successful()
 
homepage_autentication()


