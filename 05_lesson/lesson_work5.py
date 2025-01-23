from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/inputs")

input_space = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_space.send_keys('1000')
sleep(2)

input_space.clear()
input_space.send_keys('999')
sleep(2)

driver.quit()
