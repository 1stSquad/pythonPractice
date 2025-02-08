from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, _driver):
        self.driver = _driver
        self.driver.get('https://www.saucedemo.com/')

    def login(self):
        # Вводим логин и пароль
        self.driver.find_element(By.ID, "user-name").send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()