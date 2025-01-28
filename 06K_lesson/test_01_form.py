import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Видимость для pytest'a
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Создаем функцию на заполнение полей формы
def test_add_data_in_form(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    form_name = driver.find_element(By.NAME, 'first-name')
    form_name.send_keys('Иван')

    form_lastname = driver.find_element(By.NAME, 'last-name')
    form_lastname.send_keys('Петров')

    form_address = driver.find_element(By.CSS_SELECTOR, 'input[name=address]')
    form_address.send_keys('Ленина, 55-3')

    # Принципиально не увидел разницы между локатором Name и CSS_SELECTOR, решил использовать и так и так
    form_city = driver.find_element(By.CSS_SELECTOR, 'input[name=city]')
    form_city.send_keys('Москва')

    form_country = driver.find_element(By.CSS_SELECTOR, 'input[name=country]')
    form_country.send_keys('Россия')

    form_mail = driver.find_element(By.CSS_SELECTOR, 'input[name=e-mail]')
    form_mail.send_keys('test@skypro.com')

    form_phone = driver.find_element(By.CSS_SELECTOR, 'input[name=phone]')
    form_phone.send_keys('+7985899998787')

    form_job = driver.find_element(By.CSS_SELECTOR, 'input[name=job-position]')
    form_job.send_keys('QA')

    form_company = driver.find_element(By.CSS_SELECTOR, 'input[name=company]')
    form_company.send_keys('SkyPro')

    # Нажмем кнопку "принять"
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    # Проверка полей на соответствие цветов
    zip_code_red = driver.find_element(By.CSS_SELECTOR, '#zip-code')
    assert 'alert-danger' in zip_code_red.get_attribute('class')

    green_color = driver.find_elements(By.CSS_SELECTOR, '.alert-success')
    assert len(green_color) == 9
