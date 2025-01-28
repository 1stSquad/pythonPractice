import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Видимость для pytest'a
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# зайти на сайт
def test_shop(driver):
    driver.get('https://www.saucedemo.com/')

    # Вводим логин и пароль
    driver.find_element(By.ID, "user-name").send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # Добавляем в корзину нужные вещи
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    # Переходим в корзину
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    driver.find_element(By.ID, 'checkout').click()

    # Заполняем форму своими данными и жмякаем "продолжить"
    driver.find_element(By.ID, 'first-name').send_keys('Иван')
    driver.find_element(By.ID, 'last-name').send_keys('Иванов')
    driver.find_element(By.ID, 'postal-code').send_keys('101000')
    driver.find_element(By.ID, 'continue').click()

    # Проверяем итоговую сумму (должна быть ровна $58.29)
    itogo = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    total = 'Total: $58.29'
    assert itogo == total