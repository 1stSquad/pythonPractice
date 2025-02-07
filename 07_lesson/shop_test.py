from selenium import webdriver


from Pages.login_page import LoginPage
from Pages.cart_page import CartPage
from Pages.info_page import InformPage
from Pages.over_page import OverviewPage


def test_shop():
    driver = webdriver.Chrome()

    login_page = LoginPage(driver)
    login_page.login()
    cart_page = CartPage(driver)
    cart_page.cart()
    inform_page = InformPage(driver)
    inform_page.inform()
    over_page = OverviewPage(driver)
    as_is = over_page.overview()

    total = 'Total: $58.29'
    assert as_is == total

    driver.quit()