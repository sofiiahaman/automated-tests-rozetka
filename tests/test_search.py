import time
import pytest
from pages.home_page import HomePage
from pages.results_page import ResultsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_product(driver):

    home = HomePage(driver)
    results = ResultsPage(driver)


    driver.get("https://rozetka.com.ua/ua/")
    
    search_query = "ноутбук"
    home.search(search_query)

    try:
        WebDriverWait(driver, 15).until(EC.url_contains("text="))
    except Exception:

        driver.save_screenshot("cloudflare_issue.png")
        pytest.fail("URL не змінився. Можливо, з'явилася капча Cloudflare.")

    time.sleep(3)

    first_title = results.get_first_product_title()

    assert first_title, "Назви товарів не були знайдені на сторінці"

    assert search_query.lower() in first_title.lower(), \
        f"Очікували '{search_query}', але перший товар називається: '{first_title}'"