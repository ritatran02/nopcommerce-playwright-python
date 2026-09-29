import json
from pathlib import Path

from playwright.sync_api import expect

from pages.page_object.user.user_login_page_object import UserLoginPageObject
from test_data.config import Config


PROJECT_ROOT = Path(__file__).resolve().parents[2]

with open(
        PROJECT_ROOT / "test_data" / "user_data.json",
        "r",
        encoding="utf-8"
) as file:
    test_data = json.load(file)

def test_login(page):

    login_page = UserLoginPageObject(page)

    login_data = test_data["Login"]

    login_page.open()

    login_page.login(
        login_data["emailAddress"],
        Config.get_password()
    )

    assert page.locator("a.ico-logout").is_visible()