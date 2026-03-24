from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    # Кнопка купити
    BUY_BUTTON = (By.CSS_SELECTOR, "button.buy-button")

    # Заголовок кошика
    CART_HEADER = (By.XPATH, "//h2[contains(text(), 'Кошик') or contains(text(), 'Корзина')]")

    def click_buy(self):
        wait = WebDriverWait(self.driver, 10)
        buy_btn = wait.until(EC.element_to_be_clickable(self.BUY_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buy_btn)
        import time
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", buy_btn)

    def get_cart_text(self):  # (якщо ще немає)
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(self.CART_HEADER)).text