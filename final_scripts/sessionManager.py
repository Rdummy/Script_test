from selenium import webdriver
import requests

def init_driver(proxy=None, user_agent=None):
    options = webdriver.ChromeOptions

    if proxy:
        options.add_argument(f'--proxy-server={proxy}')

    if user_agent:
        options.add_argument(f'user-agent={user_agent}')

    return webdriver.Chrome(options=options)

def store_cookies(browser):
    return browser.get_cookies()

def load_cookies(browser, cookies):
    for cookie in cookies:
        browser.add_cookie(cookie)

def make_request(url, cookies):
    response =requests.get(url,cookies=requests.utils.cookiesjar_from_dict(cookies))
    return response.text

def closeBrowser(browser):
    if browser:
        browser.quit()

