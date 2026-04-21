from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    BUY_BUTTON = (By.CSS_SELECTOR, "button.buy-button")
    OPEN_CART_BUTTON = (By.CSS_SELECTOR, ".notification-message-button, .notification__wrapper .button")
    CART_HEADER = (By.XPATH, "//h2[contains(text(), 'Кошик') or contains(text(), 'Корзина')]")
    PLUS_BUTTON = (By.CSS_SELECTOR, "button[data-testid='cart-counter-increment-button']")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input[data-testid='cart-counter-input']")
    TOTAL_PRICE = (By.CSS_SELECTOR, "div[data-testid='cart-receipt-sum'] .cart-receipt__sum-price")

    def click_buy(self):
        self.click(self.BUY_BUTTON)

    def open_cart_notification(self):
        self.click(self.OPEN_CART_BUTTON)

    def get_cart_text(self):
        element = self.find_element(self.CART_HEADER)
        return element.text
    
    def increment_quantity(self):
        self.click(self.PLUS_BUTTON)

    def get_quantity(self):
        return self.find_element(self.QUANTITY_INPUT).get_attribute("value")
    
    def get_total_price(self):
        price_text = self.find_element(self.TOTAL_PRICE).text
        return "".join(filter(str.isdigit, price_text))
