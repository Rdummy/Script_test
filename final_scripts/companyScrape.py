import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
def scrapeCompanyProfile(browser, target_url):

    time.sleep(8)
    # Company Name
    Company_Name=(browser.find_elements(By.XPATH, "//h1[contains(@class, 'org-top-card-summary__title')]//span")[0].text)
    try:
        Company_Name_Verifier = (browser.find_elements(By.XPATH, "//h1[contains(@class, 'org-top-card-summary__title')][@title]")[0].text)
        confirm_comp_name= (Company_Name == Company_Name_Verifier)
    except:
        print('Verification Check has error')
    if confirm_comp_name:
        print("Success Company Name is verified and extracteds")
    print("comp1: ", Company_Name)
    print("comp2: ", Company_Name_Verifier)

    #Domain 
    showAllDetails_ariaLabel = "See all details about " + Company_Name
    xpath_base = f"//a[@aria-label='{showAllDetails_ariaLabel}']"  # Use f-string for cleaner formatting
    showAllDetailsButton = browser.find_element(By.XPATH, xpath_base)
    showAllDetailsButton.click()

    
    if(EC.url_changes(target_url)):
        print("Clicked About Company Details!")
    div_elements = (browser.find_element(By.XPATH, "//dd[contains(., 'employees')]").text)
    employees = int(''.join(i for i in div_elements if i.isdigit()))

    #domain / Website
#//dt[contains(text(), 'Website')]/following-sibling::dd[contains(text(), '.com')]/a
    linkExtractedText = (browser.find_elements(By.XPATH, ("//dt[contains(.,'Website')]/following-sibling::dd[contains(.,'.com')]/a/span"))[0].text)
    
    
    
    # Regular expression below is wrong
    # link = re.search(r'href=["\'](https?://\S+)', linkExtractedText)
    

    #industry
    industry = (browser.find_elements(By.XPATH,("//dt[contains(.,'Industry')]/following-sibling::*[1]"))[0].text)

    print("")
    print("---------------------------")
    print("Company Details")
    print("---------------------------")
    print("company_name: ", Company_Name )
    print("employee count: ", employees )
    print("company website or domain: ", linkExtractedText)
    print("linkedin url: ", target_url)
    print("Industry: ", industry)
