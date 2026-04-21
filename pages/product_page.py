import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    BUY_BUTTON = (By.CSS_SELECTOR, "button.buy-button")
    OPEN_CART_BUTTON = (By.CSS_SELECTOR, ".notification-message-button, .notification__wrapper .button")
    CART_HEADER = (By.XPATH, "//h2[contains(text(), 'Кошик') or contains(text(), 'Корзина')]")
    PLUS_BUTTON = (By.CSS_SELECTOR, "button[data-testid='cart-counter-increment-button']")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input[data-testid='cart-counter-input']")
    TOTAL_PRICE = (By.CSS_SELECTOR, "div[data-testid='cart-receipt-sum'] .cart-receipt__sum-price")
    CONTEXT_MENU = (By.CSS_SELECTOR, "button[id^='cartProductActions']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button.button--medium.button--with-icon.button--link")
    EMPTY_CART_TITLE = (By.CSS_SELECTOR, "h4.cart-dummy__heading")

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
    
    def set_quantity_manually(self, value):
        quantity_input = self.wait.until(EC.element_to_be_clickable(self.QUANTITY_INPUT))
        
        quantity_input.send_keys(value)
        quantity_input.send_keys(Keys.ENTER)

        time.sleep(1)

    def remove_product_from_cart(self):
        menu_btn = self.wait.until(EC.element_to_be_clickable(self.CONTEXT_MENU))
        menu_btn.click()

        time.sleep(0.5)

        delete_btn = self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON))
        delete_btn.click()

    def is_cart_empty(self):
        try:
            title = self.wait.until(EC.visibility_of_element_located(self.EMPTY_CART_TITLE))
            return "Кошик порожній" in title.text
        except:
            return False