"""The module contains classes for working with Form"""
import os

import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from data.data import Person
from pages.base_page import BasePage
from locators.form_locators import FormPageLocators
from generator.data_generator import create_person, file_generator

class FormPage(BasePage):
    LOCATORS = FormPageLocators()

    @allure.step("Filling the form")
    def fill_form_filds(self) -> Person:
        person = create_person()
        first, last, *other= person.full_name.split()
        path = file_generator()
        with allure.step('Finding elements'):
            first_name = self.element_is_visible(self.LOCATORS.FIRST_NAME)
            last_name = self.element_is_visible(self.LOCATORS.LAST_NAME)
            email = self.element_is_visible(self.LOCATORS.EMAIL)
            gender = self.element_is_presents(self.LOCATORS.GENDER)
            mobile = self.element_is_presents(self.LOCATORS.PHONE_NUMBER)
            date_of_birth = self.element_is_visible(self.LOCATORS.DAY_OF_BIRTH)
            subject = self.element_is_visible(self.LOCATORS.SUBJECT)
            hobby = self.element_is_presents(self.LOCATORS.HOBBY)
            upload = self.element_is_clickable(self.LOCATORS.UPLOAD_FILE)
            cur_address = self.element_is_visible(self.LOCATORS.CURRENT_ADDRESS)
            state = self.element_is_visible(self.LOCATORS.STATE)
            input_state = self.element_is_visible(self.LOCATORS.INPUT_STATE)
            city = self.element_is_visible(self.LOCATORS.CITY)
            input_city = self.element_is_visible(self.LOCATORS.INPUT_CITY)
            submit = self.element_is_clickable(self.LOCATORS.SUBMIT)

        with allure.step('Actions'):
            first_name.send_keys(first)
            last_name.send_keys(last)
            email.send_keys(person.email)
            gender.click()
            mobile.send_keys(person.phone_number)
            date_of_birth.click()
            year = Select(self.element_is_visible(self.LOCATORS.YEAR))
            year.select_by_value('1988')
            month = Select(self.element_is_visible(self.LOCATORS.MONTH))
            month.select_by_value('3')
            day = self.element_is_presents(self.LOCATORS.DAY)
            day.click()
            subject.send_keys('Math')
            subject.send_keys(Keys.RETURN)
            hobby.click()
            upload.send_keys(path)
            os.remove(path)
            cur_address.send_keys(person.current_addres)
            self.go_to_element(state)
            state.click()
            input_state.send_keys(Keys.RETURN)
            city.click()
            input_city.send_keys(Keys.RETURN)
            submit.click()
        return person

    @allure.step('Getting result')
    def form_result(self) -> list:
        result_list = self.elements_are_present(self.LOCATORS.RESULT_TABLE)
        data = list()
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        self.element_is_clickable(self.LOCATORS.CLOSE).click()
        return data






