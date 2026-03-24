from pages.home_page import HomePage

def test_search_product(driver):
    home = HomePage(driver)

    home.search("ноутбук")

    assert "ноутбук" in driver.page_source.lower()