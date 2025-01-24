from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, 'ajaxButton').click()

blue_button = WebDriverWait(driver, 16).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
)

text_alert = (driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text)
print(text_alert)

driver.quit()
