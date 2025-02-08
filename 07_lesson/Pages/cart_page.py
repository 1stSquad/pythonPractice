from selenium.webdriver.common.by import By



class CartPage:

    def __init__(self, _driver):
        self.driver = _driver

    def cart(self):
        # Добавляем в корзину нужные вещи
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

        # Переходим в корзину
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        self.driver.find_element(By.ID, 'checkout').click()