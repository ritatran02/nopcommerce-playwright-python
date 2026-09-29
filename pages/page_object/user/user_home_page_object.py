from pages.base_page import BasePage
from pages.page_ui.user.user_home_page_ui import UserHomePageUI
from pages.page_object.user.user_search_page_object import UserSearchPageObject
from test_data.config import Config


class UserHomePageObject(BasePage):

    def open(self):
        self.page.goto(
            Config.get_url(),
            wait_until="domcontentloaded"
        )

    def search_product(self, search_data):
        self.fill(
            UserHomePageUI.SEARCH_TEXTBOX,
            search_data
        )

        self.click(
            UserHomePageUI.SEARCH_BUTTON
        )

        return UserSearchPageObject(self.page)