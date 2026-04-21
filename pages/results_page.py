from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ResultsPage(BasePage):
    PRODUCT_TITLES = (By.CSS_SELECTOR, "a[rztiletitle], .goods-tile__title")
    FIRST_PRODUCT_LINK = (By.XPATH, "(//a[@class='goods-tile__heading'])[1]")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".price, .goods-tile__price-value")
    SORT_SELECT = (By.ID, "sort")
    CART_BUTTON_ON_TILE = (By.CSS_SELECTOR, "button.buy-button, .goods-tile__buy-button, rz-buy-button button")

    def get_first_product_title(self):
        element = self.find_element(self.PRODUCT_TITLES)
        return element.text.strip().lower() 
    
    def click_first_product(self):
        self.click(self.FIRST_PRODUCT_LINK)

    def get_all_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        prices = []
        for el in elements:
            clean_price = "".join(filter(str.isdigit, el.text))
            if clean_price:
                prices.append(int(clean_price))
        return prices

    def sort_by_cheap(self):
        from selenium.webdriver.support.ui import Select
        select_element = Select(self.find_element(self.SORT_SELECT))
        select_element.select_by_value("cheap")
        import time
        time.sleep(3)

    def addToCart_first_product(self):
        try:
            self.wait.until(EC.visibility_of_any_elements_located(self.CART_BUTTON_ON_TILE))

            cart_buttons = self.driver.find_elements(*self.CART_BUTTON_ON_TILE)

            self.driver.execute_script("arguments[0].click();", cart_buttons[0])
            
        except Exception as e:
            raise Exception(f"Помилка при додаванні в кошик: {str(e)}")