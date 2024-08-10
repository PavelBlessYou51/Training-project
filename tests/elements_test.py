import random

import allure
import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage


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

    @allure.feature('Test of WebTable')
    class TestWebTable:

        @allure.title('Test of adding employee')
        def test_add_employee(self, get_driver):
            count_empl_to_add = random.randint(1, 15)
            web_table_page = WebTablePage(get_driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            for i in range(count_empl_to_add):
                web_table_page.click_add_button()
                web_table_page.add_employee()
            count_added_empl = web_table_page.get_count_of_employees()
            assert count_added_empl == 3 + count_empl_to_add, "Count of emploees doesn't match"

        @allure.title('Count rows testing')
        def test_count_of_rows(self, get_driver):
            web_table_page = WebTablePage(get_driver, 'https://demoqa.com/webtables')
            rows = web_table_page.count_of_rows()
            assert rows == (10, 5, 100), "Count of rows doesn't match"

        @allure.title('Testing of earch field')
        def test_search_field(self, get_driver):
            web_table_page = WebTablePage(get_driver, 'https://demoqa.com/webtables')
            before, after = web_table_page.search_employee()
            assert before == after, "Last name doesn't match"

        @allure.title('Testing of edit employee')
        def test_edit_employee(self, get_driver):
            web_table_page = WebTablePage(get_driver, 'https://demoqa.com/webtables')
            new_salary, current_salary = web_table_page.edit_eployee()
            assert new_salary == current_salary, "Salary name doesn't match"

        @allure.title('Testing of delete employee')
        def test_delete_employee(self, get_driver):
            web_table_page = WebTablePage(get_driver, 'https://demoqa.com/webtables')
            result = web_table_page.delete_all_employee()
            assert result == 'No rows found', "Employees weren't been deleted"

    @allure.feature('Test of buttons')
    class TestButtons:

        @allure.title('Testing of double click')
        def test_double_click(self, get_driver):
            buttons_page = ButtonsPage(get_driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            result = buttons_page.double_click()
            assert result == 'You have done a double click', "The double click hasn't been perform"

        @allure.title('Testing of right click')
        def test_right_click(self, get_driver):
            buttons_page = ButtonsPage(get_driver, 'https://demoqa.com/buttons')
            result = buttons_page.right_click()
            assert result == 'You have done a right click', "The right click hasn't been perform"

        @allure.title('Testing of simple click')
        def test_simple_click(self, get_driver):
            buttons_page = ButtonsPage(get_driver, 'https://demoqa.com/buttons')
            result = buttons_page.simple_click()
            assert result == 'You have done a dynamic click', "The simple click hasn't been perform"
