from config.driver_config import driver
from pages import main
from util import verify_duplicated


def test_get_text(driver):
    page = main.MainPage(driver)
    page.open_page()
    assert page.verify_page_title()
    page.click_text_item()
    assert 'Getting Started' in page.get_title_text()
    assert verify_duplicated.is_duplicated_char(page.get_title_text())
