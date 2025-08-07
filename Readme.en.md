# Playwright Automation Testing for Demoblaze

[![RU](https://img.shields.io/badge/RU-русский-0066CC?logo=russia&logoColor=white)](https://github.com/Ewerall/PlaywrightDemoblaze/blob/main/README.md)

[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Allure Report](https://img.shields.io/badge/Allure_Report-FF4882?logo=allure&logoColor=white)](https://qameta.io/allure-report/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/Ewerall/PlaywrightDemoblaze/actions/workflows/ci.yml)

Automated testing for the [Demoblaze](https://demoblaze.com) web application:
- **26+ parameterized tests** with full functional coverage
- **End-to-End scenarios** simulating real user interactions
- **Advanced wait strategies** for "complex" web applications
- Integration with **Allure Report** and **GitHub Actions CI/CD**

## Implementation Features

- **Robust Page Object Model**  
  Adapted for sites with poor layout and dynamic loading
- **Combined waiting strategies**  
  Mix of network waits, custom JS checks, and dialog handling
- **Test data parameterization**  
  Realistic profile generation using Faker
- **Professional Allure integration**  
  Detailed reports with epics, features, and stories
- **State management**  
  Fixtures for cart cleanup and test isolation

```bash
PlaywrightDemoblaze
├── .github/              # CI/CD configuration
├── data/                 # Test data generators
├── pages/                # Page Object Model implementation
├── tests/                # 26+ parameterized tests
├── conftest.py           # Fixtures and configuration
├── pytest.ini            # Pytest settings
└── requirements.txt      # Dependencies
```

## Tech Stack

| Category | Stack |
|--|--|
| Core | Python 3.10+, Playwright, Pytest |]
| Patterns | Page Object Model (POM)|
| Reporting| Allure Framework, Allure-pytest|
| CI/CD | GitHub Actions, Allure Report CI |
| Utilities | Faker (data generation) |

## Run Tests
```
# Install dependencies
pip install -r requirements.txt
playwright install

# Run all tests
pytest --alluredir=allure-results

# Run specific test group
pytest tests/test_e2e.py -v

# Generate Allure report
allure serve allure-results
```

## Allure-отчеты
[Latest Allure Report](https://ewerall.github.io/PlaywrightDemoblaze/#suites/ac0d5a5ca3595f3896d8c76597ca74f3/3c820b7c61d675ab/ "Allure") from Github actions

## Test Cases
Testing Type | Example Scenarios | Count
|--|--|--|
End2End | Registration → Product Selection → Payment | 1+
Home page | Categories, carousel, pagination |	3+
Product page | Data validation, add to cart | 2+
Cart page| Total calculation, item removal, checkout | 1+
Users | Registration, login, feedback | 2+
Invalid | Registration, login, feedback, Payment | 4+

## Technical Challenges Solved

1. Handling "fragile" elements <br>
Custom explicit waits for dynamically loaded content:
```python
with  self.page.expect_response(lambda  response: '/pagination'  in  response.url  and  response.status  ==  200):
        self.page.locator(direction).click()
self.page.wait_for_function("""
	() => {
            const container = document.querySelector('#tbodyid');
            return container && container.children.length > 0;
        }
""", timeout=10000)
expect(self.page.locator("#tbodyid .col-lg-4").first).to_be_visible(timeout=10000)
```
2. Dialog and alert handling <br>
Specialized handlers for modal windows:

```python
with page.expect_event("dialog") as dialog_info:
    page.locator(ADD_BUTTON).click()
dialog = dialog_info.value
dialog.accept()
```

3. Network explicit wait <br>
Monitoring API requests during actions:

```python
with  self.page.expect_response("**/bycat") as  response_info:
	self.page.click(f'a:has-text("{category}")')
response  =  response_info.value
assert  response.status  ==  200
```

## Sample Run in Headed Mode

<video src='https://github.com/user-attachments/assets/1c503fa2-f8ec-4cfc-a1f5-7eefd5123ff6' width=180/>
