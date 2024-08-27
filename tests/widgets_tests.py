"""The module contains test of Widgets"""
import allure
import pytest

from pages.widgets_page import AccordianPage, AutoCompilePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage
from tests.conftest import get_driver


@allure.suite('Test of Widgets')
class TestWidgets:
    @allure.feature('Test of Accordian')
    class TestAccordianPage:

        @allure.title('Testing of accordian')
        @pytest.mark.parametrize('accordian',
                                 [('first', 'What is Lorem Ipsum?'),
                                  ('second', 'Where does it come from?'),
                                  ('third', 'Why do we use it?')])
        def test_accordian(self, get_driver, accordian):
            accordian_page = AccordianPage(get_driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            title, content = accordian_page.open_accordian(accordian[0])
            assert title == accordian[1] and len(content) > 0


    @allure.feature('Test of auto copmlite')
    class TestAutoComplitePage:

        @allure.title('Testing of auto complite')
        @pytest.mark.parametrize('type_field', [('single', 1), ('multi', 4)])
        def test_auto_complite(self, get_driver, type_field):
            auto_complite_page = AutoCompilePage(get_driver, 'https://demoqa.com/auto-complete')
            auto_complite_page.open()
            colors_before, colores_after = auto_complite_page.check_colors(*type_field)
            assert colors_before == colores_after

    @allure.feature('Test of date')
    class TestDatePickerPage:

        @allure.title('Testing of select date')
        def test_select_date(self, get_driver):
            date_picker_page = DatePickerPage(get_driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_before, date_after = date_picker_page.select_date()
            assert date_before != date_after

        @allure.title('Testing of date and time')
        def test_date_time(self, get_driver):
            date_picker_page = DatePickerPage(get_driver)
            date_before, date_after = date_picker_page.select_date_and_time()
            assert date_before != date_after

    @allure.feature('Test of the slider')
    class TestSliderPage:

        @allure.title('Testing of the slider')
        def test_slider(self, get_driver):
            slider_page = SliderPage(get_driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page.move_slider()
            assert before != after

    @allure.feature('Test of the progress bar')
    class TestProgressBarPage:

        @allure.title('Testing of the progress bar')
        def test_progress_bar(self, get_driver):
            progress_page = ProgressBarPage(get_driver, 'https://demoqa.com/progress-bar')
            progress_page.open()
            before, after = progress_page.check_progress_bar()
            assert before != after

    @allure.feature('Test of tabs')
    class TestTabsPage:

        @allure.title('Testing of tabs')
        @pytest.mark.parametrize('tab_type', ['What', 'Origin', 'Use', 'More'])
        def test_tabs(self, get_driver, tab_type):
            tabs_page = TabsPage(get_driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            title, content = tabs_page.check_tabs(tab_type)
            assert title == tab_type and len(content) != 0

    @allure.feature('Test of tips')
    class TestToolTipsPage:

        @allure.title('Testing of tips')
        @pytest.mark.parametrize('type_tip', ['Button', 'field', 'Contrary', '1.10.32'])
        def test_tips(self, get_driver, type_tip):
            tips_page = ToolTipsPage(get_driver, 'https://demoqa.com/tool-tips')
            tips_page.open()
            tip = tips_page.get_type_tip(type_tip)
            assert tip == type_tip

    @allure.feature('Test of menu')
    class TestMenuPage:

        @allure.title('Testing of menu')
        def test_menu(self, get_driver):
            menu_page = MenuPage(get_driver, 'https://demoqa.com/menu#')
            menu_page.open()
            result = menu_page.inspect_menu()
            assert result == 'Sub Sub Item 2'
