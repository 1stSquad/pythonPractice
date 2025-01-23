from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for i in range(5):
    add_button.click()

delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
print("Итого 'Delete':", len(delete_buttons))

sleep(2)

driver.quit()