import allure
import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage
from selenium.common import TimeoutException


@allure.suite('Test of elements')
class TestElements:
    @allure.feature('Test of TextBox')
    class TestTextBox:
        @allure.title('TextBox test')
        def test_text_box(self, get_driver):
            text_box_page = TextBoxPage(get_driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_form()
            output_data = text_box_page.get_output_data()
            assert input_data == output_data, "The data does not match"

    @allure.feature('Test of CheckBox')
    class TestCheckBox:

        @allure.title('CheckBox Test')
        def test_check_box(self, get_driver):
            check_box_page = CheckBoxPage(get_driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.expend_all_boxes()
            check_box_page.select_random_boxes()
            checked_boxes = check_box_page.collect_titles_of_checked_boxes()
            output = check_box_page.get_output()
            assert checked_boxes == output, "The checked boxes do not match"

    @allure.feature("Test of RadioButton")
    class TestRadioButton:

        @allure.title('RadioButton Test')
        @pytest.mark.parametrize('label_button', ['yes', 'impressive', 'no'])
        def test_radio_button(self, get_driver, label_button):
            radio_button_page = RadioButtonPage(get_driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_button(label_button)
            click_result = radio_button_page.get_result()
            assert click_result == label_button, f"Wrong '{label_button.upper()}' button result of click"

