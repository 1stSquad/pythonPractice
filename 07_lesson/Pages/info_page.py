from selenium.webdriver.common.by import By


class InformPage:

    def __init__(self, _driver):
        self.driver = _driver

    def inform(self):
        # Заполняем форму своими данными и жмякаем "продолжить"
        self.driver.find_element(By.ID, 'first-name').send_keys('Иван')
        self.driver.find_element(By.ID, 'last-name').send_keys('Иванов')
        self.driver.find_element(By.ID, 'postal-code').send_keys('101000')
        self.driver.find_element(By.ID, 'continue').click()