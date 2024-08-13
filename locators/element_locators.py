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
    CHECK_BOXES = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_OF_CHECKED_BOX = ".//ancestor::span[@class='rct-text']"
    RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonLocators:
    YES_BUTTON = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="yesRadio"]')
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="impressiveRadio"]')
    NO_BUTTON = (By.CSS_SELECTOR, 'label[class="custom-control-label disabled"][for="noRadio"]')
    RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


class WebTableLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")

    # Registration form

    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE = (By.CSS_SELECTOR, "input[id='age']")
    SALARY = (By.CSS_SELECTOR, "input[id='salary']")
    DAPARTMENT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # Table

    FILLED_FIELDS = (By.XPATH, "//div[@class='rt-tr -odd' or @class='rt-tr -even']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "div[class='-next'] button")
    SELECT_ROWS = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    FIELDS = (By.CSS_SELECTOR, "div[role='row']")

    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[id="searchBox"]')

    DELETE_EMPLOYEE = ".//span[@title='Delete']"
    EDIT_EMPLOYEE = "span[title='Edit']"
    EMPTY_LIST = (By.CSS_SELECTOR, "div[class='rt-noData']")


class ButtonsPageLocators:
    DOUBLE_CLICK = (By.CSS_SELECTOR, "#doubleClickBtn")
    RIGHT_CLICK = (By.CSS_SELECTOR, "#rightClickBtn")
    CLICK = (By.XPATH, "//button[text()='Click Me']")

    MESSAGE_DOUBLE_CLICK = (By.CSS_SELECTOR, "#doubleClickMessage")
    MESSAGE_RIGHT_CLICK = (By.CSS_SELECTOR, "#rightClickMessage")
    MESSAGE_CLICK = (By.CSS_SELECTOR, "#dynamicClickMessage")


class LinksPageLocators:
    # Links
    LINK = (By.CSS_SELECTOR, "#simpleLink")
    DYNAMIC_LINK = (By.CSS_SELECTOR, "#dynamicLink")

    # Requests
    CREATED = (By.CSS_SELECTOR, "#created")
    NO_CONTENT = (By.CSS_SELECTOR, "#no-content")
    MOVED = (By.CSS_SELECTOR, "#moved")
    BAD_REQUEST = (By.CSS_SELECTOR, "#bad-request")
    UNAUTHORIZED = (By.CSS_SELECTOR, "#unauthorized")
    FORBIDDEN = (By.CSS_SELECTOR, "#forbidden")
    NOT_FOUND = (By.CSS_SELECTOR, "#invalid-url")

    RESPONSE = (By.XPATH, "//b[2]")


class ImagesPageLocators:
    IMAGE = (By.XPATH, "(//img)[3]")
