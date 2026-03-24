from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ResultsPage(BasePage):
    PRODUCT_TITLES = (By.XPATH, "//*[contains(@class, 'title')]")

    def get_first_product_title(self):
        element = self.find_element(self.PRODUCT_TITLES)
        return element.text.lower()