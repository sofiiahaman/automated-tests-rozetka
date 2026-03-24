from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):

    SEARCH_INPUT = (By.CSS_SELECTOR, "[data-testid='search-suggest-input']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-testid='search-suggest-submit']")

    def search(self, text):
        search_field = self.find_element(self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER) 