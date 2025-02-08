from selenium import webdriver
from Pages.from_page import FormPage


def test_complete_the_form():
    # Инициализация драйвера
    driver = webdriver.Chrome()

    # Создание экземпляра страницы
    form_page = FormPage(driver)

    # Выполнение тестовых действий
    form_page.complete_the_form()
    form_page.sublime_click()
    form_page.zip_code_red()

    # Закрытие браузера
    driver.quit()