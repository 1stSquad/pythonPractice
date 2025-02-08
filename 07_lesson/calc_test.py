from selenium import webdriver
from Pages.calc_page import CalcPage


def test_calculator():
    driver = webdriver.Chrome()

    calc_page = CalcPage(driver)
    calc_page.delay()
    calc_page.calculator()
    as_is = calc_page.result()

    correct_answer = '15'
    assert as_is == correct_answer

    driver.quit()