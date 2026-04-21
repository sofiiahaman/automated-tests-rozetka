import pytest
import undetected_chromedriver as uc
import time
import os 
from pages.home_page import HomePage
from pages.results_page import ResultsPage
from pages.product_page import ProductPage

@pytest.fixture
def driver():
    driver = None 
    options = uc.ChromeOptions()

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if os.environ.get('CI'): 
        options.add_argument("--headless") 
        options.add_argument("--window-size=1920,1080")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        options.add_argument("--disable-gpu")
        options.add_argument("--blink-settings=imagesEnabled=false")

    try:
        driver = uc.Chrome(options=options)

        if not os.environ.get('CI'):
            driver.maximize_window()
            
        driver.get("https://rozetka.com.ua/ua/")
        time.sleep(5)
        print(f"\nDEBUG: Поточний заголовок сторінки: {driver.title}")
        yield driver
    except Exception as e:
        print(f"\nПомилка при запуску браузера: {e}")
        raise e 
    finally:
        if driver is not None:
            try:
                driver.quit()
            except:
                pass


@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def results_page(driver):
    return ResultsPage(driver)

@pytest.fixture
def product_page(driver):
    return ProductPage(driver)