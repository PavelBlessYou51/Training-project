"""The module contains test of form"""
import allure

from pages.form_page import FormPage

@allure.suite('Test of form')
class TestForm:
    def test_form(self, get_driver):
       form_page = FormPage(get_driver, 'https://demoqa.com/automation-practice-form')
       form_page.open()
       form_data = form_page.fill_form_filds()
       form_result = form_page.form_result()
       assert [form_data.full_name, form_data.email] == [form_result[0], form_result[
           1]], 'The form has not been fill'