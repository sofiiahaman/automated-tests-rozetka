from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    BUY_BUTTON = (By.CSS_SELECTOR, "button.buy-button")
    OPEN_CART_BUTTON = (By.CSS_SELECTOR, ".notification-message-button, .notification__wrapper .button")
    CART_HEADER = (By.XPATH, "//h2[contains(text(), 'Кошик') or contains(text(), 'Корзина')]")

    def click_buy(self):
        self.click(self.BUY_BUTTON)

    def open_cart_notification(self):
        self.click(self.OPEN_CART_BUTTON)

    def get_cart_text(self):
        element = self.find_element(self.CART_HEADER)
        return element.text