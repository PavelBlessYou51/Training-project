"""The module contains classes for working with Alerts, Windows and Frames"""
import time

import allure

from locators.alerts_windows_frame_page_locators import BrowserWindowPageLocators, AlertsPageLocators, FramePageLocators, NestedFramesPageLocators, ModalDialogPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    LOCATORS = BrowserWindowPageLocators()

    @allure.step('Open a new tab or window')
    def open_new_tab_or_window(self, button_type: str) -> str:
        type_dict = {
            'tab': self.LOCATORS.NEW_TAB,
            'window': self.LOCATORS.NEW_WINDOW
        }
        self.element_is_clickable(type_dict[button_type]).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_visible(self.LOCATORS.NEW_TAB_WIN_TEXT).text
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return text

class AlertsPage(BasePage):

    LOCATORS = AlertsPageLocators()

    @allure.step('Open the simple alert')
    def simple_alert(self) -> str:
        button = self.element_is_clickable(self.LOCATORS.SIMPLE_ALERT)
        button.click()
        alert = self.driver.switch_to.alert
        text_alert = alert.text
        alert.accept()
        return text_alert

    @allure.step('Open the delay alert')
    def delay_alert(self) -> str:
        button = self.element_is_clickable(self.LOCATORS.DELAY_ALERT)
        button.click()
        time.sleep(6)
        alert = self.driver.switch_to.alert
        text_alert = alert.text
        alert.accept()
        return text_alert

    @allure.step('Open the confirm alert')
    def confirm_alert(self) -> str:
        button = self.element_is_clickable(self.LOCATORS.CONFIRM_ALERT)
        button.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        result = self.element_is_visible(self.LOCATORS.RESULT_CONFIRM)
        result_text = result.text
        return result_text

    @allure.step('Open the promt alert')
    def promt_alert(self) -> str:
        button = self.element_is_clickable(self.LOCATORS.PROMT_ALERT)
        button.click()
        alert = self.driver.switch_to.alert
        alert.send_keys('Pavel')
        alert.accept()
        result = self.element_is_visible(self.LOCATORS.RESULT_PROMT)
        result_text = result.text
        return result_text

class FramesPage(BasePage):

    LOCATORS = FramePageLocators()

    @allure.step('Check the frame')
    def check_frame(self, frame_num) -> tuple[str, str, str]:
        frame_dict = {
            'first': self.LOCATORS.FIRST_FRAME,
            'second': self.LOCATORS.SECOND_FRAME
        }
        frame = self.element_is_presents(frame_dict[frame_num])
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.element_is_visible(self.LOCATORS.FRAME_TEXT).text
        self.driver.switch_to.default_content()
        return width, height, text

class NestedFramePage(BasePage):

    LOCATORS = NestedFramesPageLocators()

    @allure.step('Check the nested frame')
    def check_nested_frame(self) -> str:
        parent_frame = self.element_is_visible(self.LOCATORS.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        child_frame = self.element_is_visible(self.LOCATORS.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_frame_text = self.element_is_visible(self.LOCATORS.CHILD_FRAME_TEXT).text
        return child_frame_text

class ModalDialogsPage(BasePage):

    LOCATORS = ModalDialogPageLocators()

    @allure.step('Checking the modal dialog windows')
    def check_dialog_windows(self) -> tuple[str, str]:
        self.element_is_clickable(self.LOCATORS.SMALL_MODAL).click()
        title_small_dialog = self.element_is_visible(self.LOCATORS.SMALL_MODAL_TITLE).text
        self.element_is_clickable(self.LOCATORS.CLOSE_BUTTON).click()
        self.element_is_clickable(self.LOCATORS.LARGE_MODAL).click()
        title_large_dialog = self.element_is_visible(self.LOCATORS.LARGE_MODAL_TITLE).text
        return title_small_dialog, title_large_dialog


