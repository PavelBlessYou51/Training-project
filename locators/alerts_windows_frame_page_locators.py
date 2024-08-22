"""The module contains locators from Alerts, Frames and Windows section"""

from selenium.webdriver.common.by import By

class BrowserWindowPageLocators:

    NEW_TAB = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id='windowButton']")

    NEW_TAB_WIN_TEXT = (By.CSS_SELECTOR, "#sampleHeading")

class AlertsPageLocators:

    SIMPLE_ALERT = (By.CSS_SELECTOR, "button[id='alertButton']")
    DELAY_ALERT = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_ALERT = (By.CSS_SELECTOR, "button[id='confirmButton']")
    RESULT_CONFIRM = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMT_ALERT = (By.CSS_SELECTOR, "button[id='promtButton']")
    RESULT_PROMT = (By.CSS_SELECTOR, "span[id='promptResult']")

class FramePageLocators:

    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    FRAME_TEXT = (By.CSS_SELECTOR, "#sampleHeading")

class NestedFramesPageLocators:

    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_FRAME_TEXT = (By.XPATH, "//p[contains(text(), 'Child')]")

class ModalDialogPageLocators:

    SMALL_MODAL = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    LARGE_MODAL = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
