"""The module contains classes for working with interactions"""
import random
import time
from collections import namedtuple

import allure
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from locators.interaction_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DragabblePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    LOCATORS = SortablePageLocators()

    @allure.step('Change order of the list')
    def change_list_order(self) -> tuple[list[str], list[str]]:
        elements, current_order = self.get_items_with_titles(self.LOCATORS.LIST_ITEMS)
        for _ in range(random.randint(1, 5)):
            source, target = random.sample(elements, k=2)
            self.action_drag_and_drop(source, target)
        *other, new_order = self.get_items_with_titles(self.LOCATORS.LIST_ITEMS)
        return current_order, new_order

    @allure.step('Change order of the grid')
    def change_grid_order(self) -> tuple[list[str], list[str]]:
        self.element_is_visible(self.LOCATORS.GRID_TAB).click()
        elements, current_order = self.get_items_with_titles(self.LOCATORS.GRID_ITEMS)
        for _ in range(random.randint(1, 5)):
            source, target = random.sample(elements, k=2)
            self.action_drag_and_drop(source, target)
        *other, new_order = self.get_items_with_titles(self.LOCATORS.GRID_ITEMS)
        return current_order, new_order


class SelectablePage(BasePage):
    LOCATORS = SelectablePageLocators()

    @allure.step('Select list items')
    def select_list_items(self) -> tuple[list[WebElement], list[str], list[str]]:
        elements = self.elements_are_visible(self.LOCATORS.LIST_ITEMS)
        title_selected_elements = list()
        for _ in range(random.randint(1, 4)):
            element = random.choice(elements)
            title_selected_elements.append(element.text)
            element.click()
        selected_elements, result_titles = self.get_items_with_titles(self.LOCATORS.LIST_ACTIVE_ITEMS)
        return selected_elements, title_selected_elements, result_titles

    @allure.step('Select grid items')
    def select_grid_items(self) -> tuple[list[WebElement], list[str], list[str]]:
        self.element_is_visible(self.LOCATORS.GRID_TAB).click()
        elements = self.elements_are_visible(self.LOCATORS.GRID_ITEMS)
        title_selected_elements = list()
        for _ in range(random.randint(1, 9)):
            element = random.choice(elements)
            title_selected_elements.append(element.text)
            element.click()
        selected_elements, result_titles = self.get_items_with_titles(self.LOCATORS.GRID_ACTIVE_ITEMS)
        return selected_elements, title_selected_elements, result_titles


class ResizablePage(BasePage):
    LOCATORS = ResizablePageLocators()

    def get_width_and_height(self, element: WebElement) -> tuple[str, str]:
        width, height = element.value_of_css_property('width'), element.value_of_css_property('height')
        return width, height

    @allure.step('Change size of box')
    def change_box_size(self):
        elem = self.element_is_visible(self.LOCATORS.BOX)
        start_width, start_height = self.get_width_and_height(elem)
        handle = self.element_is_visible(self.LOCATORS.HANDLE)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(handle, -100, -100)
        action.perform()
        min_width, min_height = self.get_width_and_height(elem)
        action.drag_and_drop_by_offset(handle, 400, 200)
        action.perform()
        max_width, max_height = self.get_width_and_height(elem)
        return start_width, start_height, min_width, min_height, max_width, max_height


class DroppablePage(BasePage):
    LOCATORS = DroppablePageLocators()

    @allure.step('Simple drop')
    def simple_drop(self) -> tuple[str, str, str]:
        drag = self.element_is_visible(self.LOCATORS.DRAG)
        drop = self.element_is_visible(self.LOCATORS.DROP)
        color_before = drop.value_of_css_property('background-color')
        self.action_drag_and_drop(drag, drop)
        color_after = drop.value_of_css_property('background-color')
        title = drop.text
        return color_before, color_after, title

    @allure.step('Accept drop')
    def accept_drop(self) -> tuple[str, str, str, str]:
        self.element_is_visible(self.LOCATORS.ACCEPT_TAB).click()
        not_acceptable = self.element_is_visible(self.LOCATORS.NOT_ACCEPTABLE)
        drop = self.element_is_visible(self.LOCATORS.ACCEPRT_DROP)
        color_before = drop.value_of_css_property('background-color')
        self.action_drag_and_drop(not_acceptable, drop)
        color_not_accept = drop.value_of_css_property('background-color')
        acceptable = self.element_is_visible(self.LOCATORS.ACCEPTABLE)
        self.action_drag_and_drop(acceptable, drop)
        color_accept = drop.value_of_css_property('background-color')
        title = drop.text
        return color_before, color_not_accept, color_accept, title

    @allure.step('Revert drop')
    def revert_drop(self, block_type: str) -> tuple[str, str, str, str]:
        block_dict = {
            'revert': self.LOCATORS.REVERTABLE,
            'not_revert': self.LOCATORS.NOT_REVERTABLE
        }
        self.element_is_visible(self.LOCATORS.REVERT_TAB).click()
        drag = self.element_is_visible(block_dict[block_type])
        top_before, left_before = drag.value_of_css_property('top'), drag.value_of_css_property('left')
        drop = self.element_is_visible(self.LOCATORS.REVERT_DROP)
        self.action_drag_and_drop(drag, drop)
        time.sleep(3)
        top_after, left_after = drag.value_of_css_property('top'), drag.value_of_css_property('left')
        return top_before, left_before, top_after, left_after


class DragabblePage(BasePage):
    LOCATORS = DragabblePageLocators()

    @allure.step('Simple drag')
    def simple_drag(self) -> tuple[str, str, str, str]:
        drag = self.element_is_visible(self.LOCATORS.DRAG)
        top_before, left_before = drag.value_of_css_property('top'), drag.value_of_css_property('left')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(drag, 50, 50)
        action.perform()
        top_after, left_after = drag.value_of_css_property('top'), drag.value_of_css_property('left')
        return top_before, left_before, top_after, left_after

    @allure.step('Axis drag')
    def axis_drag(self, block_type) -> tuple[str, str, str, str]:
        self.element_is_visible(self.LOCATORS.AXIS_TAB).click()
        block_dict = {
            'x': self.LOCATORS.ONLY_X,
            'y': self.LOCATORS.ONLY_Y
        }
        drag = self.element_is_visible(block_dict[block_type])
        top_before, left_before = drag.value_of_css_property('top'), drag.value_of_css_property('left')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(drag, 50, 50)
        action.perform()
        top_after, left_after = drag.value_of_css_property('top'), drag.value_of_css_property('left')
        return top_before, left_before, top_after, left_after