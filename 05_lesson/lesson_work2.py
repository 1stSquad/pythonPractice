from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
blue_button.click()

sleep(3)
driver.quit()