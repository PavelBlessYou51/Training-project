"""The module contains locators from Elements section"""
from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Input locators

    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    # Output loctors

    FULL_NAME_OUTPUT = (By.CSS_SELECTOR, '#name')
    EMAIL_OUTPUT = (By.CSS_SELECTOR, '#email')
    CURRENT_ADDRESS_OUTPUT = (By.CSS_SELECTOR, 'p[id="currentAddress"]')
    PERMANENT_ADDRESS_OUTPUT = (By.CSS_SELECTOR, 'p[id="permanentAddress"]')


class CheckBoxPageLoactors:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
