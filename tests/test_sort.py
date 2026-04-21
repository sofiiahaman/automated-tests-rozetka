import pytest
import time
from pages.home_page import HomePage
from pages.results_page import ResultsPage

def test_sort_cheap_first(driver):
    home = HomePage(driver)
    results = ResultsPage(driver)

    driver.get("https://rozetka.com.ua/ua/")
    home.search("клавіатура")
    
    results.sort_by_cheap()
    
    prices = results.get_all_product_prices()
    if len(prices) >= 2:
        assert prices[0] <= prices[1], f"Сортування не спрацювало: {prices[0]} > {prices[1]}"