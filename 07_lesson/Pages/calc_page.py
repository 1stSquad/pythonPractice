from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, _driver):
        self.driver = _driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    def delay(self):
        delay = self.driver.find_element(By.CSS_SELECTOR, 'input#delay')
        delay.clear()
        delay.send_keys('45')

    def calculator(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

        WebDriverWait(self.driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    def result(self):
        res = self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        return res
