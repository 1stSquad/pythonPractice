from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/textinput")

text = driver.find_element(By.ID, 'newButtonName')
text.send_keys('SkyPro')

driver.find_element(By.ID, 'updatingButton').click()
text_alert = driver.find_element(By.ID, 'updatingButton').text
print(text_alert)

driver.quit()