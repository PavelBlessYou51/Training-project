"""The module contains classes for working with WebElements"""
import datetime
import os
import random
import requests

import allure
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.data_generator import create_person, string_handler
from locators.element_locators import TextBoxPageLocators, CheckBoxPageLoactors, RadioButtonLocators, WebTableLocators, \
    ButtonsPageLocators, LinksPageLocators, ImagesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    LOCATORS = TextBoxPageLocators()

    @allure.step('Fill the form')
    def fill_form(self) -> tuple[str, str, str, str]:
        with allure.step('Generating data'):
            person = create_person()
            full_name = person.full_name
            email = person.email
            current_address = person.current_addres
            current_address = current_address.replace('\n', ' ')
            permanent_address = person.permanent_addres
            permanent_address = permanent_address.replace('\n', ' ')
        with allure.step('Sending data to the form'):
            self.element_is_visible(self.LOCATORS.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.LOCATORS.EMAIL).send_keys(email)
            self.element_is_visible(self.LOCATORS.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.LOCATORS.PERMANENT_ADDRESS).send_keys(permanent_address)
            button = self.element_is_clickable(self.LOCATORS.SUBMIT)
            self.go_to_element(button)
            button.click()
        return full_name, email, current_address, permanent_address

    @allure.step('Get data for checking')
    def get_output_data(self) -> tuple[str, str, str, str]:
        with allure.step('Get data from output fields'):
            output_data = (
                self.element_is_visible(self.LOCATORS.FULL_NAME_OUTPUT).text,
                self.element_is_visible(self.LOCATORS.EMAIL_OUTPUT).text,
                self.element_is_visible(self.LOCATORS.CURRENT_ADDRESS_OUTPUT).text,
                self.element_is_visible(self.LOCATORS.PERMANENT_ADDRESS_OUTPUT).text
            )
            full_name, email, current_address, permanent_address = tuple(
                map(lambda data: data.split(':')[1], output_data))
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    LOCATORS = CheckBoxPageLoactors()

    @allure.step('Expending all boxes')
    def expend_all_boxes(self) -> None:
        expend_button = self.element_is_visible(self.LOCATORS.EXPAND_ALL_BUTTON)
        expend_button.click()

    @allure.step('Selecting random boxes')
    def select_random_boxes(self) -> None:
        with allure.step('Finding boxes'):
            check_boxes = self.elements_are_visible(self.LOCATORS.CHECK_BOXES)
            count_of_boxes = len(check_boxes)
        with allure.step('Click on each found box'):
            for click in range(10, count_of_boxes):
                box_index = random.randint(1, count_of_boxes - 1)
                elem = check_boxes[box_index]
                self.go_to_element(elem)
                elem.click()

    @allure.step('Collecting titles of checked boxes')
    def collect_titles_of_checked_boxes(self) -> list[str]:
        with allure.step('Finding checked boxes'):
            checked_boxes = self.elements_are_visible(self.LOCATORS.CHECKED_ITEMS)
            list_of_titles = list()
        with allure.step('Getting titles'):
            for box in checked_boxes:
                box_title = box.find_element(By.XPATH, self.LOCATORS.TITLE_OF_CHECKED_BOX).text
                box_title_for_check = string_handler(box_title)
                list_of_titles.append(box_title_for_check)
        return list_of_titles

    @allure.step('Getting output result')
    def get_output(self) -> list[str]:
        output_result = self.elements_are_present(self.LOCATORS.RESULT)
        result_titles = [elem.text for elem in output_result]
        return result_titles


class RadioButtonPage(BasePage):
    LOCATORS = RadioButtonLocators()

    @allure.step('Clicks button')
    def click_button(self, label_button: str) -> None:
        button_locators = {
            "yes": self.LOCATORS.YES_BUTTON,
            "no": self.LOCATORS.NO_BUTTON,
            "impressive": self.LOCATORS.IMPRESSIVE_BUTTON
        }
        element = self.element_is_visible(button_locators[label_button])
        element.click()

    @allure.step('Gets result')
    def get_result(self) -> str:
        result_text = None
        try:
            element = self.element_is_visible(self.LOCATORS.RESULT)
            result_text = element.text
            result_text = result_text.lower()
        except TimeoutException:
            print("The element wasn't found")
        return result_text


class WebTablePage(BasePage):
    LOCATORS = WebTableLocators()

    @allure.step('Click add button')
    def click_add_button(self) -> None:
        add_button = self.element_is_clickable(self.LOCATORS.ADD_BUTTON)
        add_button.click()

    @allure.step('Add employee')
    def add_employee(self) -> None:
        employee = create_person()

        with allure.step("Finding fields"):
            first_name = self.element_is_visible(self.LOCATORS.FIRST_NAME)
            last_name = self.element_is_visible(self.LOCATORS.LAST_NAME)
            email = self.element_is_visible(self.LOCATORS.EMAIL)
            age = self.element_is_visible(self.LOCATORS.AGE)
            salary = self.element_is_visible(self.LOCATORS.SALARY)
            department = self.element_is_visible(self.LOCATORS.DAPARTMENT)
            submit_button = self.element_is_clickable(self.LOCATORS.SUBMIT_BUTTON)

        with allure.step("Sending data"):
            first, last, *other = employee.full_name.split()
            first_name.send_keys(first)
            last_name.send_keys(last)
            email.send_keys(employee.email)
            age.send_keys(employee.age)
            salary.send_keys(employee.salary)
            department.send_keys(employee.department)
            submit_button.click()

    @allure.step('Get count of employees')
    def get_count_of_employees(self) -> int:
        next_button = self.element_is_visible(self.LOCATORS.NEXT_BUTTON)
        count_of_employees = len(self.elements_are_visible(self.LOCATORS.FILLED_FIELDS))
        while self.is_element_enable(next_button):
            self.go_to_element(next_button)
            next_button.click()
            count_of_employees += len(self.elements_are_visible(self.LOCATORS.FILLED_FIELDS))
        return count_of_employees

    @allure.step('Count rows')
    def count_of_rows(self) -> tuple[int, int, int]:
        current_count_rows = len(self.elements_are_visible(self.LOCATORS.FIELDS)) - 1
        select_element = self.element_is_visible(self.LOCATORS.SELECT_ROWS)
        select_rows = Select(select_element)
        select_rows.select_by_value('5')
        five_rows = len(self.elements_are_visible(self.LOCATORS.FIELDS)) - 1
        select_rows.select_by_value('100')
        hundred_rows = len(self.elements_are_visible(self.LOCATORS.FIELDS)) - 1
        return current_count_rows, five_rows, hundred_rows

    def search_employee(self):
        with allure.step('Get count of employees before searching and random last name'):
            select_element = self.element_is_visible(self.LOCATORS.SELECT_ROWS)
            select_rows = Select(select_element)
            select_rows.select_by_value('100')
            employees_before = self.elements_are_visible(self.LOCATORS.FILLED_FIELDS)
            empl_for_search = random.choice(employees_before)
            last_name_before = empl_for_search.find_element(By.XPATH, "(//div[@class='rt-td'])[2]").text
        with allure.step('Get count of employees before searching and random last name'):
            search_field = self.element_is_visible(self.LOCATORS.SEARCH_FIELD)
            search_field.send_keys(last_name_before)
            employees_after = self.elements_are_visible(self.LOCATORS.FILLED_FIELDS)
            last_name_after = employees_after[0].find_element(By.XPATH, "(//div[@class='rt-td'])[2]").text
        return last_name_before, last_name_after

    def edit_eployee(self) -> tuple[str, str]:
        new_salary = '1000000'
        with allure.step('Getting random employee to edit'):
            random_employee = random.choice(self.elements_are_visible(self.LOCATORS.FILLED_FIELDS))
            edit_button = random_employee.find_element(By.CSS_SELECTOR, self.LOCATORS.EDIT_EMPLOYEE)
            self.go_to_element(edit_button)
            edit_button.click()
        with allure.step('Send new salary'):
            salary_field = self.element_is_visible(self.LOCATORS.SALARY)
            salary_field.clear()
            salary_field.send_keys(new_salary)
            submit_button = self.element_is_clickable(self.LOCATORS.SUBMIT_BUTTON)
            submit_button.click()
        with allure.step('Getting current salary'):
            current_salary = random_employee.find_element(By.XPATH, './/div[5]').text
        return new_salary, current_salary

    def delete_all_employee(self) -> str:
        employees = self.elements_are_visible(self.LOCATORS.FILLED_FIELDS)
        with allure.step('Delete all employees'):
            for empl in employees:
                try:
                    employee = empl.find_element(By.XPATH, self.LOCATORS.DELETE_EMPLOYEE)
                except StaleElementReferenceException:
                    empl = self.element_is_visible(self.LOCATORS.FILLED_FIELDS)
                    employee = empl.find_element(By.XPATH, self.LOCATORS.DELETE_EMPLOYEE)
                employee.click()
        result = self.element_is_visible(self.LOCATORS.EMPTY_LIST).text
        return result


class ButtonsPage(BasePage):
    LOCATORS = ButtonsPageLocators()

    def double_click(self) -> str:
        with allure.step('Double click on te button'):
            button = self.element_is_clickable(self.LOCATORS.DOUBLE_CLICK)
            actions = ActionChains(self.driver)
            actions.double_click(button)
            actions.perform()
        with allure.step('Getting message'):
            element = self.element_is_visible(self.LOCATORS.MESSAGE_DOUBLE_CLICK)
            message = element.text
            return message

    def right_click(self) -> str:
        with allure.step('Right click on te button'):
            button = self.element_is_clickable(self.LOCATORS.RIGHT_CLICK)
            actions = ActionChains(self.driver)
            actions.context_click(button)
            actions.perform()
        with allure.step('Getting message'):
            element = self.element_is_visible(self.LOCATORS.MESSAGE_RIGHT_CLICK)
            message = element.text
            return message

    def simple_click(self) -> str:
        with allure.step('Simple click on te button'):
            button = self.element_is_clickable(self.LOCATORS.CLICK)
            button.click()
        with allure.step('Getting message'):
            element = self.element_is_visible(self.LOCATORS.MESSAGE_CLICK)
            message = element.text
            return message


class LinksPage(BasePage):
    LOCATORS = LinksPageLocators()

    def open_links(self, link_type) -> tuple[str, str]:
        with allure.step('Creating the dict with locators'):
            links_dict = {
                'static': self.LOCATORS.LINK,
                'dynamic': self.LOCATORS.DYNAMIC_LINK
            }
        with allure.step('Use the link'):
            link = self.element_is_visible(links_dict[link_type])
            link_url = link.get_attribute('href')
            link.click()
        with allure.step('Switching windows'):
            windows = self.driver.window_handles
            current_window = self.driver.current_window_handle
            self.driver.switch_to.window(windows[1])
            new_tab_url = self.driver.current_url
            self.driver.close()
            self.driver.switch_to.window(current_window)
        return link_url, new_tab_url

    def use_api_links(self, response_type, answer) -> bool:
        with allure.step('Creating the dict with locators'):
            request_dict = {
                'created': self.LOCATORS.CREATED,
                'no-content': self.LOCATORS.NO_CONTENT,
                'moved': self.LOCATORS.MOVED,
                'bad_request': self.LOCATORS.BAD_REQUEST,
                'unauthorized': self.LOCATORS.UNAUTHORIZED,
                'fordidden': self.LOCATORS.FORBIDDEN,
                'not_found': self.LOCATORS.NOT_FOUND
            }
        with allure.step('Getting the link name and response'):
            link = self.element_is_visible(request_dict[response_type])
            self.go_to_element(link)
            link.click()
            result = self.elemement_has_text(self.LOCATORS.RESPONSE, answer)
        return result


class ImagesPage(BasePage):
    LOCATORS = ImagesPageLocators()

    def make_screen(self) -> str:
        self.element_is_visible(self.LOCATORS.IMAGE)
        screen_name = 'screen' + f'-{datetime.date.today()}' + '.png'
        screen_path = os.getcwd().rsplit('\\', 1)[0] + r'\screenshots'
        os.makedirs(screen_path, exist_ok=True)
        path = screen_path + '\\' + screen_name
        self.get_screen_shot(path)
        return path

    def get_image(self) -> str:
        element = self.element_is_visible(self.LOCATORS.IMAGE)
        url = element.get_attribute('src')
        response = requests.get(url)
        image_path = os.getcwd().rsplit('\\', 1)[0] + r'\images'
        image_name = 'image' + f'-{datetime.date.today()}' + '.jpg'
        os.makedirs(image_path, exist_ok=True)
        path = image_path + '\\' + image_name
        with open(path, 'wb') as img_file:
            img_file.write(response.content)
        return path


