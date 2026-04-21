# Automated UI Tests for Rozetka

This repository contains automated UI tests for the **[Rozetka](https://rozetka.com.ua/)** online store. The tests cover core user scenarios such as product search, sorting, and cart management.

[View HTML Report](https://sofiiahaman.github.io/automated-tests-rozetka/)

---

## Tech Stack

- **Python**
- **Selenium WebDriver** – browser automation
- **Pytest** – test framework
- **pytest-html** – HTML test reports

---

## Project Structure
```text
.
├── .github/workflows   # CI configuration 
├── pages               # Page Object Model (POM) classes
├── tests               # Test cases
├── conftest.py         # Pytest fixtures and setup
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Dependencies
├── index.html          # Example test report (pytest-html)
└── .gitignore
```

---

## Implemented Test Cases

### Search

- `test_search_product`  
  Verifies that a product can be successfully found using the search functionality.

---

### Sorting

- `test_sort_cheap_first`  
  Ensures that products are correctly sorted by price (lowest first).

---

### Cart Functionality

- `test_add_to_cart_from_results`  
  Checks that a product can be added to the cart directly from search results.

- `test_change_product_quantity_in_cart`  
  Verifies that the quantity of a product in the cart can be updated.

- `test_negative_product_quantity_validation`  
  Ensures that invalid (negative) quantity values are properly handled and rejected.

- `test_remove_product_from_cart`  
  Confirms that a product can be removed from the cart.

---
Test Reports
---

After execution, an HTML report will be generated.
It includes:

- Test results (passed/failed)
- Execution time
- Error details (if any)

Design Approach
---

The project follows the Page Object Model (POM) pattern:

- Separates test logic from UI interactions
- Improves maintainability and readability
- Makes tests easier to scale

## Setup & Installation

### 1. Clone the repository

```bash
git clone 
```

### 2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests
Run all tests:
```
pytest
```

Run tests with HTML report:
```
pytest --html=index.html --self-contained-html
```
