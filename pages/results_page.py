from pages.home_page import HomePage
from pages.results_page import ResultsPage

def test_search_product(driver):
    home = HomePage(driver)
    results = ResultsPage(driver)

    search_query = "ноутбук"

    home.search(search_query)

    assert "search" in driver.current_url

    first_title = results.get_first_product_title()
    assert search_query in first_title.lower()