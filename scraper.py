from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector
import re

strPattern = re.compile(r"(?<=\s)\w.+(?=\n+)")

USERNAME = '' # Insert your linkedin user
PASSWORD = '' # Insert your linkedin password
searchString = 'site:linkedin.com/in/ AND "Data Scientist" AND "Argentina"'
DRIVERPATH = '/usr/bin/chromedriver'

def filter_links(linksList):
    links = []
    linkedinStr = 'linkedin.com/'
    translateStr = 'google.com'

    for link in linksList:
        if (linkedinStr in link) and (not translateStr in link):
            links.append(link)

    return(links)

# Open Browser Session
# In case you're using a different browser, check 
# https://www.selenium.dev/downloads/
# For Chrome in particular 
# https://sites.google.com/a/chromium.org/chromedriver/
# Please note that the driver version has to match **exactly** with your
# browser version and placed in the same path as browser executable
driver = webdriver.Chrome(DRIVERPATH)

#Get webpage
driver.get('https://www.linkedin.com')
username = driver.find_element_by_id('session_key')
password = driver.find_element_by_id('session_password')
signInButton = driver.find_element_by_class_name(\
                    'sign-in-form__submit-button')
#Insert login info
username.send_keys(USERNAME)
sleep(0.5)
password.send_keys(PASSWORD)
sleep(0.5)
signInButton.click()
sleep(1)

# Find candidates in google

driver.get('https://www.google.com')
sleep(3)
searchQuery = driver.find_element_by_name('q')
searchQuery.send_keys(searchString)
searchQuery.send_keys(Keys.RETURN)
linkedinUrls = driver.find_elements_by_css_selector(".yuRUbf [href]")
linkedinUrls = [s.get_attribute('href') for s in linkedinUrls]
links = filter_links(linkedinUrls)

# Iterate over each result
for link in links:
    driver.get(link)
    sleep(5)
    # Send the complete webpage to the Selector
    sel = Selector(text=driver.page_source)
    # Find strings by CSS classes, clean them with regular expressions
    rawName = sel.xpath('//*[starts-with(@class, \
        "inline t-24 t-black t-normal break-words")]/text()').extract_first()
    name = strPattern.findall(rawName)[0]
    rawPosition = sel.xpath('//*[starts-with(@class,\
        "mt1 t-18 t-black t-normal break-words")]/text()').extract_first()
    position = strPattern.findall(rawPosition)[0]
    rawLocation = sel.xpath('//*[starts-with(@class, \
        "t-16 t-black t-normal inline-block")]/text()').extract_first()
    location = strPattern.findall(rawLocation)[0]
    compnUniversity = sel.xpath('//*[starts-with(@class,' \
        '"text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp '\
        'lt-line-clamp--multi-line ember-view")]/text()').extract()
    company = strPattern.findall(compnUniversity[0])[0]
    if len(compnUniversity) > 1:
        university = strPattern.findall(compnUniversity[1])[0]

    print('Name: ',name)
    print('Position: ',position)
    print('Location: ',location)
    print('Company: ',company)
    print('University: ',university)

driver.quit()
