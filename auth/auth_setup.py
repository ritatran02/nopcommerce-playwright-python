import json
from pathlib import Path

from playwright.sync_api import sync_playwright, expect

from test_data.config import Config
from pages.page_object.user.user_login_page_object import UserLoginPageObject


PROJECT_ROOT = Path(__file__).resolve().parent.parent

with open(
        PROJECT_ROOT / "test_data" / "user_data.json",
        "r",
        encoding="utf-8"
) as file:
    test_data = json.load(file)


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    login_page = UserLoginPageObject(page)

    login_data = test_data["Login"]

    login_page.open()

    login_page.login(
        login_data["emailAddress"],
        Config.get_password()
    )

    expect(page.locator("a.ico-logout")).to_be_visible()

    context.storage_state(
        path=PROJECT_ROOT / "auth" / "user.json"
    )

    browser.close()