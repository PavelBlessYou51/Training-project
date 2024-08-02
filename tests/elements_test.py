import allure

from pages.elements_page import TextBoxPage


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
