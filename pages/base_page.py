"""The module contains basic methods for working with pages of site"""
import os

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver, url: str = None):
        self.driver = driver
        self.url = url

    def open(self) -> None:
        """Open browser window"""
        self.driver.get(self.url)

    # Methods for seeking elements on the web-page

    def element_is_visible(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: tuple[str, str], timeout: int = 5) -> list[WebElement]:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_presents(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator: tuple[str, str], timeout: int = 5) -> list[WebElement]:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def is_element_enable(self, element):
        return element.is_enabled()

    def elemement_has_text(self, locator: tuple[str, str], text: str, timeout: int = 5) -> bool:
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def get_screen_shot(self, path) -> None:
        self.driver.get_screenshot_as_file(path)

    def get_root_dir(self) -> str:
        root_dir = os.getcwd().rsplit('\\', 1)[0]
        os.makedirs(root_dir, exist_ok=True)
        return root_dir
