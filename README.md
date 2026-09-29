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

> `.env`, `auth/user.json` and `test-result`
