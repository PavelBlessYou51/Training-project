"""The module contains classes for working with widgets"""
import random
import time
from collections import namedtuple

import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from locators.widgets_page_locators import AccordianPageLocators, AutoComplitePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
from pages.base_page import BasePage
from generator.data_generator import get_colors, date_generator


class AccordianPage(BasePage):
    LOCATORS = AccordianPageLocators()

    @allure.step('Open accordian and get content')
    def open_accordian(self, accordian):
        accordian_dict = {
            'first': {
                'title': self.LOCATORS.FIRST_LOREM,
                'content': self.LOCATORS.FIRST_LOREM_CONTENT
            },

            'second': {
                'title': self.LOCATORS.SECOND_LOREM,
                'content': self.LOCATORS.SECOND_LOREM_CONTENT
            },

            'third': {
                'title': self.LOCATORS.THIRD_LOREM,
                'content': self.LOCATORS.THIRD_LOREM_CONTENT
            }
        }
        current_accordian = self.element_is_visible(accordian_dict[accordian]['title'])
        current_accordian.click()
        accordian_title = current_accordian.text
        accordian_content = self.element_is_visible(accordian_dict[accordian]['content']).text
        return accordian_title, accordian_content


class AutoCompilePage(BasePage):
    LOCATORS = AutoComplitePageLocators()

    @allure.step('Ckeck color fields')
    def check_colors(self, type_field: str, count_colors: int = 1) -> tuple[list, list]:
        with allure.step('Getting random colors'):
            colors_before = get_colors(random.randint(1, count_colors))
        Locators = namedtuple('Locators', ['field', 'color'])
        single = Locators(self.LOCATORS.SINGLE_COLOR_FIELD, self.LOCATORS.SINGLE_COLOR)
        multi = Locators(self.LOCATORS.MULTIPLE_COLOR_FIELD, self.LOCATORS.MULTIPLE_COLORS)
        dict_of_locators = {
            'single': single,
            'multi': multi,
        }
        with allure.step('Sending colors to field'):
            field_locator = self.element_is_visible(dict_of_locators[type_field].field)
            for color in colors_before:
                field_locator.send_keys(color)
                field_locator.send_keys(Keys.RETURN)
        with allure.step('Getting result colors'):
            color_locators = self.elements_are_visible(dict_of_locators[type_field].color)
            colors_after = [color.text for color in color_locators]
        return colors_before, colors_after


class DatePickerPage(BasePage):
    LOCATORS = DatePickerPageLocators()

    def set_year_or_month_with_select(self, locator: tuple[str, str], value: str):
        select = Select(self.element_is_visible(locator))
        if value.isdigit():
            select.select_by_value(value)
        else:
            select.select_by_visible_text(value)

    def set_time_day_month_year(self, locator: tuple[str, str], value: str):
        items = self.elements_are_present(locator)
        for item in items:
            if item.text == value:
                print(value)
                item.click()
                break

    @allure.step('Select date')
    def select_date(self) -> tuple[str, str]:
        my_date = date_generator()
        date_field = self.element_is_presents(self.LOCATORS.SELECT_DATE_FIELD)
        date_before = date_field.get_attribute('value')
        date_field.click()
        with allure.step('Set year'):
            self.set_year_or_month_with_select(self.LOCATORS.SELECT_YEAR, my_date.year)
        with allure.step('Set month'):
            self.set_year_or_month_with_select(self.LOCATORS.SELECT_MONTH, my_date.month)
        with allure.step('Set day'):
            self.set_time_day_month_year(self.LOCATORS.SELECT_DAYS, my_date.day)
        date_after = date_field.get_attribute('value')
        return date_before, date_after

    @allure.step('Select data and time')
    def select_date_and_time(self) -> tuple[str, str]:
        my_date = date_generator()
        date_field = self.element_is_presents(self.LOCATORS.DATE_TIME_FIELD)
        date_before = date_field.get_attribute('value')
        date_field.click()
        with allure.step('Set year'):
            self.element_is_visible(self.LOCATORS.DATE_TIME_YEAR_LIST).click()
            self.set_time_day_month_year(self.LOCATORS.DATE_TIME_YEARS, '2020')
        with allure.step('Set month'):
            self.element_is_visible(self.LOCATORS.DATE_TIME_MONTH_LIST).click()
            self.set_time_day_month_year(self.LOCATORS.DATE_TIME_MONTHS, my_date.month)
        with allure.step('Set day'):
            self.set_time_day_month_year(self.LOCATORS.SELECT_DAYS, my_date.day)
        with allure.step('Set time'):
            self.set_time_day_month_year(self.LOCATORS.TIME, my_date.time)
        date_after = date_field.get_attribute('value')
        return date_before, date_after


class SliderPage(BasePage):
    LOCATORS = SliderPageLocators()

    @allure.step('Check slider')
    def move_slider(self) -> tuple[str, str]:
        slider = self.element_is_visible(self.LOCATORS.SLIDER)
        slider_value = self.element_is_visible(self.LOCATORS.SLIDER_VALUE)
        value_before = slider_value.get_attribute('value')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(slider, random.randint(-25, 75), 0)
        action.perform()
        value_after = slider_value.get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    LOCATORS = ProgressBarPageLocators()

    @allure.step('Check the progress bar')
    def check_progress_bar(self) -> tuple[str, str]:
        start_button = self.element_is_clickable(self.LOCATORS.START_BUTTON)
        progress_bar = self.element_is_presents(self.LOCATORS.PROGRESS_BAR)
        progress_before = progress_bar.get_attribute('aria-valuenow')
        start_button.click()
        time.sleep(4)
        start_button.click()
        progress_after = progress_bar.get_attribute('aria-valuenow')
        return progress_before, progress_after


class TabsPage(BasePage):
    LOCATORS = TabsPageLocators()

    @allure.step("Check tabs")
    def check_tabs(self, tab_type: str) -> tuple[str, str]:
        tabs_dict = {
            'What': (self.LOCATORS.WHAT_TAB, self.LOCATORS.CONTENT_WHAT),
            'Origin': (self.LOCATORS.ORIGIN_TAB, self.LOCATORS.CONTENT_ORIGIN),
            'Use': (self.LOCATORS.USE_TAB, self.LOCATORS.CONTENT_USE),
            'More': (self.LOCATORS.MORE_TAB, None)
        }
        tab = self.element_is_visible(tabs_dict[tab_type][0])
        tab.click()
        tab_title = tab.text
        tab_content = self.element_is_visible(tabs_dict[tab_type][1]).text
        return tab_title, tab_content

class ToolTipsPage(BasePage):
    LOCATORS = ToolTipsPageLocators()

    @allure.step('Check tips')
    def get_type_tip(self, type_tip):
        dict_tips = {
            'Button': self.LOCATORS.BUTTON,
            'field': self.LOCATORS.FIELD,
            'Contrary': self.LOCATORS.COUNTRY,
            '1.10.32': self.LOCATORS.DIGIT
        }
        hover_element = self.element_is_visible(dict_tips[type_tip])
        action = ActionChains(self.driver)
        action.move_to_element(hover_element).perform()
        tip_text = self.element_is_visible(self.LOCATORS.TIP, 6).text
        tip_result = tip_text.rsplit(maxsplit=1)[-1]
        return tip_result

class MenuPage(BasePage):
    LOCATORS = MenuPageLocators()

    @allure.step('Inspect menu')
    def inspect_menu(self):
        action = ActionChains(self.driver)
        main_item = self.element_is_visible(self.LOCATORS.MAIN_ITEM)
        action.move_to_element(main_item).perform()
        sub_item = self.element_is_visible(self.LOCATORS.SUB_ITEM)
        action.move_to_element(sub_item).perform()
        sub_sub_item = self.element_is_visible(self.LOCATORS.SUB_SUB_ITEM)
        action.move_to_element(sub_sub_item).perform()
        result_text = sub_sub_item.text
        return result_text