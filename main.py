from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from getpass import getpass

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://10.104.8.111:8443/racommon/NSLogin.jsp?redirect=%2Fconsole%2F")
print(driver.title)

# Load nGenius Web page
search = driver.find_element_by_id('details-button')
search.send_keys(Keys.RETURN)

# Load nGenius Web page
search = driver.find_element_by_id('proceed-link')
search.send_keys(Keys.RETURN)

usernameText = input("Enter your LCL username: ")
passwordText = getpass("Enter your password: ")

# nGenius Auto Login
search = driver.find_element_by_id('usernameText')
search.send_keys(usernameText)

# nGenius Auto Login
search = driver.find_element_by_id('passwordText')
search.send_keys(passwordText)

# nGenius Login
search = driver.find_element_by_id('submitBtn')
search.send_keys(Keys.RETURN)

time.sleep(6)
# Search Modules
search = driver.find_element_by_id('ember474')
search.send_keys('locations')
time.sleep(5)
button = driver.find_element_by_class_name('module ')
button.click()

time.sleep(5)
button = driver.find_element_by_class_name("ui-button ui-corner-all ui-icon-ns-filter_up_off")
button.click()

time.sleep(10)
InputText = input("Enter Store #: ")
search = driver.find_element_by_id('gs_sm-name')
search.send_keys(InputText)



time.sleep(10)

#driver.quit()