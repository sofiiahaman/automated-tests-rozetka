import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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

    for i in range(3):
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "section.goods-grid, rz-grid"))
            )
            break 
        except WebDriverException as e:
            if "no such execution context" in str(e) and i < 2:
                time.sleep(1) 
                continue
            raise e

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


def test_negative_product_quantity_validation(driver, home_page, results_page, product_page):
    driver.get("https://rozetka.com.ua/ua/")

    home_page.search("iphone")
 
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "section.goods-grid, rz-grid"))
    )

    time.sleep(1)

    results_page.addToCart_first_product()
 
    product_page.open_cart_notification()
   
    product_page.set_quantity_manually("-5")

    actual_quantity = product_page.get_quantity()

    assert "-" not in actual_quantity, "Система дозволила ввести символ мінуса!"

    quantity_int = int(actual_quantity)
    assert quantity_int >= 1, f"Кількість не може бути меншою за 1, але отримали {quantity_int}"
        
    print(f"DEBUG: Тест пройшов. Система відхилила '-5' і встановила '{actual_quantity}'")


def test_remove_product_from_cart(driver, home_page, results_page, product_page):
    driver.get("https://rozetka.com.ua/ua/")

    home_page.search("iphone")
 
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "section.goods-grid, rz-grid"))
    )

    results_page.addToCart_first_product()

    product_page.open_cart_notification()

    product_page.remove_product_from_cart()

    assert product_page.is_cart_empty(), "Помилка: Після видалення товару кошик не став порожнім!"
    
    print("Товар успішно видалено, кошик порожній.")