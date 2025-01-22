from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/entry_ad")

driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

sleep(5)
driver.quit()