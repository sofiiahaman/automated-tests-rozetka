import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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

def test_change_product_quantity_in_cart(driver, home_page, results_page, product_page):
    driver.get("https://rozetka.com.ua/ua/")

    home_page.search("iphone")

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "section.goods-grid, rz-grid"))
    )

    time.sleep(1)

    results_page.addToCart_first_product()
    
    product_page.open_cart_notification()

    price_for_one = int(product_page.get_total_price())

    product_page.increment_quantity()
 
    WebDriverWait(driver, 10).until(
        lambda d: int(product_page.get_total_price()) > price_for_one
    )

    assert product_page.get_quantity() == "2"
    assert int(product_page.get_total_price()) > price_for_one