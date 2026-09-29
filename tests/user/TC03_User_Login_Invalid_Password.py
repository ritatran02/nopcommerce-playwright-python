import json
from pathlib import Path

from pages.page_object.user.user_login_page_object import UserLoginPageObject


PROJECT_ROOT = Path(__file__).resolve().parents[2]

with open(
        PROJECT_ROOT / "test_data" / "user_data.json",
        "r",
        encoding="utf-8"
) as file:
    test_data = json.load(file)

def test_login_with_invalid_password(page):

    login_page = UserLoginPageObject(page)

    failed_login_data = test_data["FailedLogin"]

    login_page.open()

    login_page.login(
        failed_login_data["emailAddress"],
        failed_login_data["password"]
    )

    assert page.locator("a.ico-logout").is_visible()