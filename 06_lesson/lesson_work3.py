from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 11).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), 'Done!')
)

source = driver.find_element(By.ID, 'award').get_attribute('src')
print(source)

driver.quit()