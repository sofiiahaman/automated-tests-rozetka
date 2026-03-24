import pytest
import undetected_chromedriver as uc
import time

@pytest.fixture
def driver():
    options = uc.ChromeOptions()

    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")

    driver = uc.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://rozetka.com.ua/ua/")

    time.sleep(5)

    yield driver

    driver.quit()