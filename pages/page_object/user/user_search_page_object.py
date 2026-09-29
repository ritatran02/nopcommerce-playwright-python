from pages.base_page import BasePage
from pages.page_ui.user.user_search_page_ui import UserSearchPageUI


class UserSearchPageObject(BasePage):

    def get_product_name_list(self):
        return self.page.locator(
            UserSearchPageUI.PRODUCT_NAME_TEXT
        ).all_inner_texts()