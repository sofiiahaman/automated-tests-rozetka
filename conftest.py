import pytest
import undetected_chromedriver as uc
import time

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