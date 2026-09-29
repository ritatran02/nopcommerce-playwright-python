import json
from pathlib import Path

from pages.page_object.user.user_register_page_object import UserRegisterPageObject
from test_data.config import Config
from test_data.data_config import DataConfig


PROJECT_ROOT = Path(__file__).resolve().parents[2]

with open(
        PROJECT_ROOT / "test_data" / "user_data.json",
        "r",
        encoding="utf-8"
) as file:
    test_data = json.load(file)


def test_register(page):

    register_page = UserRegisterPageObject(page)
    data = DataConfig.get_data()

    user_data = test_data["Register"].copy()

    user_data["first_name"] = data.get_first_name()
    user_data["last_name"] = data.get_last_name()
    user_data["email"] = data.get_email_address()
    user_data["password"] = Config.get_password()
    user_data["confirm_password"] = Config.get_password()

    register_page.open()
    register_page.register(user_data)

    assert "registration completed" in (
        register_page.get_register_success_message().lower()
    )