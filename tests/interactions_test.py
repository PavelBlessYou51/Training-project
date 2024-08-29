"""The module contains test of Interactions"""
import allure
import pytest

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage


@allure.suite('Test of Interactions')
class TestInteractions:
    @allure.feature('Test of Sortable elements')
    class TestSortablePage:

        @allure.title('Testing of Sortable list')
        def test_sortable_list(self, get_driver):
            sortable_page = SortablePage(get_driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            current_order, new_order = sortable_page.change_list_order()
            assert current_order != new_order

        @allure.title('Testing of Sortable grid')
        def test_sortable_grid(self, get_driver):
            sortable_page = SortablePage(get_driver)
            current_order, new_order = sortable_page.change_grid_order()
            assert current_order != new_order

    @allure.feature('Test of selected elements')
    class TestSelectablePage:

        @allure.title('Testing of selected items of list')
        def test_selected_list_items(self, get_driver):
            selectable_page = SelectablePage(get_driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            selected_elements, title_selected_elements, result_titles = selectable_page.select_list_items()
            assert selected_elements and title_selected_elements.sort() == result_titles.sort()

        @allure.title('Testing of selected items of grid')
        def test_selected_grid_items(self, get_driver):
            selectable_page = SelectablePage(get_driver)
            selected_elements, title_selected_elements, result_titles = selectable_page.select_grid_items()
            assert selected_elements and title_selected_elements.sort() == result_titles.sort()

    @allure.feature('Test of resizable elements')
    class TestResizablePage:

        @allure.title('Testing of resizable element')
        def test_resizable_elem(self, get_driver):
            resizable_page = ResizablePage(get_driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            sizes = resizable_page.change_box_size()
            assert sizes == ('200px', '200px', '150px', '150px', '500px', '300px')

    @allure.feature('Test of droppable elements')
    class TestDroppablePage:

        @allure.title('Testing of simple drop')
        def test_simple_drop(self, get_driver):
            droppable_page = DroppablePage(get_driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            before, after, title = droppable_page.simple_drop()
            assert before != after and title == 'Dropped!'

        @allure.title('Testing of acceptable drop')
        def test_accept_drop(self, get_driver):
            droppable_page = DroppablePage(get_driver)
            before, not_accept, accept, title = droppable_page.accept_drop()
            assert before == not_accept
            assert not_accept != accept and title == 'Dropped!'

        @allure.title('Testing of revertable drop')
        @pytest.mark.parametrize('block_type', ['revert', 'not_revert'])
        def test_revert_drop(self, get_driver, block_type):
            droppable_page = DroppablePage(get_driver)
            top_before, left_before, top_after, left_after = droppable_page.revert_drop(block_type)
            if block_type == 'revert':
                assert (top_before, left_before) == (top_after, left_after)
            else:
                assert (top_before, left_before) != (top_after, left_after)

    @allure.feature('Test of dragabble elements')
    class TestDragabblePage:

        @allure.title('Testing of simple drag')
        def test_simple_drag(self, get_driver):
            dragabble_page = DragabblePage(get_driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            top_before, left_before, top_after, left_after = dragabble_page.simple_drag()
            assert top_before != top_after and left_before != left_after

        @allure.title('Testing of axis drag')
        @pytest.mark.parametrize('block_type', ['x', 'y'])
        def test_axis_drag(self, get_driver, block_type):
            dragabble_page = DragabblePage(get_driver, 'https://demoqa.com/dragabble')
            top_before, left_before, top_after, left_after = dragabble_page.axis_drag(block_type)
            if block_type == 'x':
                assert top_before == top_after == '0px' and left_before != left_after
            else:
                assert left_before == left_after == '0px' and top_before != top_after
