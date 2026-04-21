import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.results_page import ResultsPage
from pages.product_page import ProductPage

def test_add_to_cart_from_results(driver):
    home = HomePage(driver)
    results = ResultsPage(driver)
    product = ProductPage(driver)

    driver.get("https://rozetka.com.ua/ua/")

    home.search("iphone")
    WebDriverWait(driver, 15).until(EC.url_contains("text=iphone"))
    
    time.sleep(2) 

    results.addToCart_first_product()

    product.open_cart_notification()

    cart_title = product.get_cart_text()

    assert "Кошик" in cart_title or "Корзина" in cart_title