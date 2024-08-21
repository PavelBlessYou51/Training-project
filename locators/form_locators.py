"""The module contains locators from Practice form page"""
import random

from selenium.webdriver.common.by import By

class FormPageLocators:

    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input[id='userNumber']")

    DAY_OF_BIRTH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DAY = (By.CSS_SELECTOR, "div[class*='react-datepicker__day react-datepicker__day--023']")

    SUBJECT = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBY = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    STATE = (By.CSS_SELECTOR, "div[id='state']")
    INPUT_STATE = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    CITY = (By.CSS_SELECTOR, "div[id='city']")
    INPUT_CITY = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")
    CLOSE = (By.CSS_SELECTOR, "button[id='closeLargeModal']")