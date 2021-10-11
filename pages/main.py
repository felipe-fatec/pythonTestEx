from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

URL = 'https://selenium-python.readthedocs.io/'

class MainPageLocators(object):
    """Locators here"""
    TEXT_ITEM = (By.XPATH, "//*[contains(text(),'Getting Started')]")
    TEXT_TITLE = (By.XPATH, "// h1[contains(text(), 'Getting Started')]")


class BasePage(object):
    """Base Page Object"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """PageObject of the main page """

    def open_page(self):
        self.driver.get(URL)

    def verify_page_title(self):
        return 'Selenium with Python' in self.driver.title

    def click_text_item(self):
        """Click the Getting stated item"""

        element = self.driver.find_element(*MainPageLocators.TEXT_ITEM)
        element.click()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(MainPageLocators.TEXT_TITLE))

    def get_title_text(self):
        element = self.driver.find_element(*MainPageLocators.TEXT_TITLE)
        return element.text
