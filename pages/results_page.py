from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ResultsPage(BasePage):
    PRODUCT_TITLES = (By.XPATH, "//*[contains(@class, 'title')]")

    first_product_xpath = "(//a[contains(@class, 'tile-title')])[1]"

    def get_first_product_title(self):
        element = self.find_element(self.PRODUCT_TITLES)
        return element.text.lower()
    
    def click_first_product_safely(self):
        element = self.find_element(self.FIRST_PRODUCT_XPATH)
        element.click()