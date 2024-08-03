import allure

from pages.elements_page import TextBoxPage, CheckBoxPage


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
