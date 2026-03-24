import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.results_page import ResultsPage
from pages.product_page import ProductPage

def test_add_to_cart(driver):
    home = HomePage(driver)
    results = ResultsPage(driver)
    product = ProductPage(driver)

    driver.get("https://rozetka.com.ua/ua/")

    home.search("iphone")
    print("URL після пошуку:", driver.current_url)

    wait = WebDriverWait(driver, 15)

    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/ua/')]")))
    products = driver.find_elements(By.XPATH, "//a[contains(@href, '/ua/')]")

    print("К-сть товарів:", len(products))

    first_link = products[0]

    driver.execute_script("arguments[0].scrollIntoView(true);", first_link)
    driver.execute_script("arguments[0].click();", first_link)

    driver.switch_to.window(driver.window_handles[-1])

    product.click_buy()

    cart_title = product.get_cart_text()

    assert "Кошик" in cart_title or "Корзина" in cart_title