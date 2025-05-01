from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get('https://itcareerhub.de')
payment_methods = driver.find_element(By.LINK_TEXT, 'Zahlungsarten')
assert payment_methods
payment_methods.click()
time.sleep(5)
driver.save_screenshot('payment_methods.png')
driver.quit()