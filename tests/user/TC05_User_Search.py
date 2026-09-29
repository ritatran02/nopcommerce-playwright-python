from pages.page_object.user.user_home_page_object import UserHomePageObject


def test_search_product(page):

    home_page = UserHomePageObject(page)

    home_page.open()

    search_page = home_page.search_product("book")

    product_name_list = search_page.get_product_name_list()

    assert len(product_name_list) > 0

    for product_name in product_name_list:
        assert "book" in product_name.lower(), (
            f"Product name does not contain search keyword: {product_name}"
        )