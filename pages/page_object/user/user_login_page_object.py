from pages.base_page import BasePage
from pages.page_ui.user.user_login_page_ui import UserLoginPageUI
from test_data.config import Config


class UserLoginPageObject(BasePage):

    def open(self):
        self.page.goto(
            Config.get_url() + "login",
            wait_until="domcontentloaded"
        )

    def enter_email(self, email):
        self.fill(
            UserLoginPageUI.EMAIL,
            email
        )

    def enter_password(self, password):
        self.fill(
            UserLoginPageUI.PASSWORD,
            password
        )

    def click_login(self):
        self.click(
            UserLoginPageUI.LOGIN_BUTTON
        )

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()