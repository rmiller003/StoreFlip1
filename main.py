from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://10.104.8.111:8443/racommon/NSLogin.jsp?redirect=%2Fconsole%2F")
print(driver.title)

search = driver.find_element_by_id('details-button')
search.send_keys(Keys.RETURN)

search = driver.find_element_by_id('proceed-link')
search.send_keys(Keys.RETURN)

search = driver.find_element_by_id('usernameText')
search.send_keys("rmiller_adm")

search = driver.find_element_by_id('passwordText')
search.send_keys("Trust30bonD")

search = driver.find_element_by_id('submitBtn')
search.send_keys(Keys.RETURN)

time.sleep(10)

#driver.quit()