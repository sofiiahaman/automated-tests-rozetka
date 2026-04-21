import pytest
import undetected_chromedriver as uc
import time
from pages.home_page import HomePage
from pages.results_page import ResultsPage
from pages.product_page import ProductPage

@pytest.fixture
def driver():
    driver = None 
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        
        driver = uc.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://rozetka.com.ua/ua/")
        time.sleep(5)
        yield driver
    except Exception as e:
        print(f"\nПомилка при запуску браузера: {e}")
        raise e 
    finally:
        if driver is not None:
            driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def results_page(driver):
    return ResultsPage(driver)

@pytest.fixture
def product_page(driver):
    return ProductPage(driver)