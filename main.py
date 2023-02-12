import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://siamik3.upnjatim.ac.id/siamik2022/html/siamik/login2023.asp")

assert "Sistem Informasi Akademik UPN Veteran Jawa Timur" in driver.title
soup = BeautifulSoup(driver.page_source, 'html.parser')
all_string = soup.find_all('h2')[0].get_text()
elem = driver.find_element(By.NAME, "npm")
elem.clear()
elem.send_keys("YOUR NPM")
elem = driver.find_element(By.NAME, "pass")
elem.clear()
elem.send_keys("YOUR PASSWORD")
elem = driver.find_element(By.NAME, "cap")
elem.clear()
elem.send_keys(all_string)
elem.send_keys(Keys.RETURN)
print("CAPTCHA : ", all_string)
print("Login Success")

if "No results found." in driver.page_source:
    driver.close()
    print("Login Failed")

time.sleep(1)
