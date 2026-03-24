from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    SEARCH_INPUT = (By.CSS_SELECTOR, "[data-testid='search-suggest-input']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-testid='search-suggest-submit']")

    def search(self, text):
        self.type(self.SEARCH_INPUT, text)
        self.click(self.SEARCH_BUTTON)