from selenium.webdriver.common.by import By



class OverviewPage:

    def __init__(self, _driver):
        self.driver = _driver

    def overview(self):
        # Заносим итоговую сумму в переменную
        itogo = self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        return itogo

    # def assert_sum(self):
    #     total = self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    #     print(total)
    #     assert total == 'Total: $58.29'