from playwright.sync_api import expect


def test_authenticated_user(authenticated_page):

    authenticated_page.goto(
        "http://demo.nopcommerce/",
        wait_until="domcontentloaded"
    )

    expect(
        authenticated_page.locator("a.ico-logout")
    ).to_be_visible()