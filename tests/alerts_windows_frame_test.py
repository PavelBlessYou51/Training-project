import allure
import pytest

from pages.alerts_windows_frame_page import BrowserWindowPage, AlertsPage, FramesPage, NestedFramePage, ModalDialogsPage

@allure.suite("Test of Alerts, Windows and Frames")
class TestAlertsWindowsFrames:
    @allure.feature('Test of new tab and window')
    class TestBrowserWindows:

        @allure.title('Tab and windows test')
        @pytest.mark.parametrize('button_type', ['tab', 'window'])
        def test_new_tab_or_window(self, get_driver, button_type):
            browser_page = BrowserWindowPage(get_driver, 'https://demoqa.com/browser-windows')
            browser_page.open()
            text = browser_page.open_new_tab_or_window(button_type)
            assert text == 'This is a sample page'

    @allure.feature('Test of alerts')
    class TestAlertPage:

        @allure.title('Testing of the simple alert')
        def test_simple_alert(self, get_driver):
            alert_page = AlertsPage(get_driver, 'https://demoqa.com/alerts')
            alert_page.open()
            result = alert_page.simple_alert()
            assert result == 'You clicked a button'

        @allure.title('Testing of the delay alert')
        def test_delay_alert(self, get_driver):
            alert_page = AlertsPage(get_driver)
            result = alert_page.delay_alert()
            assert result == 'This alert appeared after 5 seconds'

        @allure.title('Testing of the confirm alert')
        def test_confirm_alert(self, get_driver):
            alert_page = AlertsPage(get_driver)
            result = alert_page.confirm_alert()
            assert result == 'You selected Ok'

        @allure.title('Testing of the promt alert')
        def test_promt_alert(self, get_driver):
            alert_page = AlertsPage(get_driver)
            result = alert_page.promt_alert()
            assert result == 'You entered Pavel'

    @allure.feature('Test of frames')
    class TestFrame:

        @allure.title('Testing of frame')
        @pytest.mark.parametrize('frame_num', ['first', 'second'])
        def test_frame(self, get_driver, frame_num):
            frame_page = FramesPage(get_driver, 'https://demoqa.com/frames')
            frame_page.open()
            result = frame_page.check_frame(frame_num)
            if frame_num == 'first':
                assert result == ('500px', '350px', 'This is a sample page')
            else:
                assert result == ('100px', '100px', 'This is a sample page')

    @allure.feature('Test of nested frame')
    class TestNestedFrame:

        @allure.title('Testing of nested frame')
        def test_nested_frame(self, get_driver):
            nested_frame_page = NestedFramePage(get_driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            result = nested_frame_page.check_nested_frame()
            assert result == 'Child Iframe'

    @allure.feature('Test of modal dialog windows')
    class TestModalDialogsPage:

        @allure.title('Testing of modal dialog windows')
        def test_modal_dialogs(self, get_driver):
            modal_page = ModalDialogsPage(get_driver, 'https://demoqa.com/modal-dialogs')
            modal_page.open()
            result = modal_page.check_dialog_windows()
            assert result == ('Small Modal', 'Large Modal')
