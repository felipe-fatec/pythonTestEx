import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    _driver = webdriver.Firefox()
    yield _driver
    _driver.quit()
