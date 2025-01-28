import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Видимость для pytest'a
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Заходим на сайт
def test_calc(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    # Находим и очищаем поле delay
    driver.find_element(By.ID, 'delay').clear()
    driver.find_element(By.ID, 'delay').send_keys('45')

    # Нажимаем нужные кнопки ("7+8=")
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    # Ждем 45 секунд до получения ответа
    please_wait = WebDriverWait(driver, 46)
    please_wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15')
    )

    # Проверка правильности сложения
    result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    correct_answer = '15'
    assert result == correct_answer