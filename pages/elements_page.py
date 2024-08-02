"""The module contains classes for working with WebElements"""
import allure

from pages.base_page import BasePage
from generator.data_generator import create_person
from locators.element_locators import TextBoxPageLocators


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
            full_name, email, current_address, permanent_address = tuple(map(lambda data: data.split(':')[1], output_data))
        return full_name, email, current_address, permanent_address
