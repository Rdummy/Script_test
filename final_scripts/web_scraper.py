from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import random
 
#My Function Imports
from companyScrape import scrapeCompanyProfile 
from authService import authenticate_user

browser = webdriver.Firefox()
url = "https://www.linkedin.com/"
browser.get(url)
browser.implicitly_wait(30)
raw_html = browser.page_source
authenticated = False

session_cookies = browser.get_cookies()
with open("session_cookies.txt", 'w') as file:
    file.write(str(session_cookies))

with open("session_cookies.txt", 'r') as file:
    stored_cookies=eval(file.read())

for cookie in stored_cookies:
    browser.add_cookie(cookie)

target_url="https://www.linkedin.com/company/adobe/"
user_matrix = [["carlosmiguel.villanueva27@gmail.com", "L&GAnnex100%", "lgAnnex100%"],
               ["kiarakayecornelia@gmail.com", "Valdecoa100%", "VAldecoa100%"]]

try:
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[@data-test-id='hero__headline' and //h1[contains(text(),'Welcome to your professional community')]]"))
    )
except:
    print("Error: Loaded Content indicators changed or content not loaded within timeout")
    browser.quit()
    exit()

if not authenticated:
    authenticate_user(browser, url, user_matrix, authenticated)

#Start Scraping
    browser.get(target_url)
    scrapeCompanyProfile(browser, target_url)
    time.sleep(15)
