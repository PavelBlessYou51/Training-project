"""The module contains locators from Widgets page"""

from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_LOREM = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECOND_LOREM = (By.CSS_SELECTOR, "div[id='section2Heading']")
    THIRD_LOREM = (By.CSS_SELECTOR, "div[id='section3Heading']")
    FIRST_LOREM_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECOND_LOREM_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    THIRD_LOREM_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")


class AutoComplitePageLocators:
    MULTIPLE_COLOR_FIELD = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTIPLE_COLORS = (By.CSS_SELECTOR, "div[class='css-12jo7m5 auto-complete__multi-value__label']")

    SINGLE_COLOR_FIELD = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
    SINGLE_COLOR = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")

class DatePickerPageLocators:
    SELECT_DATE_FIELD = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    SELECT_DAYS = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_TIME_FIELD = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class ='react-datepicker__month-dropdown-container react-datepicker__month-dropdown-container--scroll']")
    DATE_TIME_MONTHS = (By.CSS_SELECTOR, "div[class ='react-datepicker__month-option']")
    DATE_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class ='react-datepicker__year-read-view']")
    DATE_TIME_YEARS = (By.CSS_SELECTOR, "div[class ='react-datepicker__year-option']")
    TIME = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")

class SliderPageLocators:
    SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "#sliderValue")

class ProgressBarPageLocators:
    START_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESS_BAR = (By.CSS_SELECTOR, "#progressBar div")

class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, "#demo-tab-what")
    ORIGIN_TAB = (By.CSS_SELECTOR, "#demo-tab-origin")
    USE_TAB = (By.CSS_SELECTOR, "#demo-tab-use")
    CONTENT_WHAT = (By.CSS_SELECTOR, "#demo-tabpane-what p")
    CONTENT_ORIGIN = (By.CSS_SELECTOR, "#demo-tabpane-origin p")
    CONTENT_USE = (By.CSS_SELECTOR, "#demo-tabpane-use p")
    MORE_TAB = (By.CSS_SELECTOR, "#demo-tab-more")

class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    FIELD = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
    COUNTRY = (By.XPATH, "//div[@id='texToolTopContainer']/a[1]")
    DIGIT = (By.XPATH, "//div[@id='texToolTopContainer']/a[2]")
    TIP = (By.CSS_SELECTOR, "div[class='tooltip-inner']")

class MenuPageLocators:
    MAIN_ITEM = (By.CSS_SELECTOR, "ul[id='nav'] li:nth-of-type(2)")
    SUB_ITEM = (By.CSS_SELECTOR, "ul[id='nav'] li:nth-of-type(2) ul li:nth-of-type(3)")
    SUB_SUB_ITEM = (By.CSS_SELECTOR, "ul[id='nav'] li:nth-of-type(2) ul li:nth-of-type(3) ul li:nth-of-type(2)")

