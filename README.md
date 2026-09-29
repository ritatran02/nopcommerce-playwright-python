# NopCommerce Playwright Python Automation

UI Automation Testing Framework for nopCommerce using Python, Playwright and Pytest.

## Tech Stack

* Python 3.13
* Playwright 1.62.0
* Pytest
* Page Object Model (POM)
* JSON Test Data
* Faker
* Python-dotenv
* Playwright Trace Viewer
* Git/GitHub

## Key Features

* Page Object Model with reusable `BasePage`
* Page UI and Page Object separation
* Data-driven testing with JSON
* Dynamic test data generation using Faker
* Environment-based configuration using `.env`
* Playwright auto-waiting
* Playwright `expect()` assertions
* Trace Viewer for failed test debugging
* Authentication reuse with `storage_state`

## Project Structure

```text
nopcommerce-playwright-python/
│
├── auth/
│   └── auth_setup.py
│
├── pages/
│   ├── page_object/
│   │   ├── admin/
│   │   └── user/
│   ├── page_ui/
│   │   ├── admin/
│   │   └── user/
│   └── base_page.py
│
├── test_data/
│   ├── config.py
│   ├── data_config.py
│   └── user_data.json
│
├── tests/
│   └── user/
│       ├── TC01_User_Register.py
│       ├── TC02_User_Login.py
│       ├── TC03_User_Login_Invalid_Password.py
│       ├── TC04_User_Authenticated.py
│       └── TC05_User_Search.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

> `.env`, `auth/user.json` and `test-results/` are local files/directories and are excluded from Git.

## Test Scenarios

* Register successfully
* Login successfully
* Login with invalid password
* Reuse authenticated session with `storage_state`
* Search product

## Test Data & Configuration

Test data is maintained separately using JSON files.

Dynamic registration data such as first name, last name and email address is generated using Faker.

Sensitive environment configuration such as application URL and password is stored in `.env` and excluded from Git.

## Authentication

Playwright `storage_state` is used to save and reuse an authenticated browser session.

The authentication flow is:

```text
Login
  ↓
Save storage state
  ↓
auth/user.json
  ↓
Create new browser context
  ↓
Reuse authenticated session
```

## Trace & Debugging

Playwright Trace Viewer is enabled for failed tests.

When a test fails, a trace file is generated under:

```text
test-results/
```

The trace contains screenshots, DOM snapshots and test execution information to help investigate failures.

## Run Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/user/TC05_User_Search.py
```

Run tests with visible browser:

```bash
pytest --headed
```

## Project Notes

This project is created as a Playwright Python automation practice and portfolio demonstration.

The project focuses on demonstrating Playwright-specific automation skills including auto-waiting, browser contexts, authentication state reuse, Trace Viewer and UI automation with Pytest.
