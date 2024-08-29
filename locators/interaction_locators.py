"""The module contains locators from Interactions page"""

from selenium.webdriver.common.by import By


class SortablePageLocators:
    # List
    LIST_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-list div[class='list-group-item list-group-item-action']")

    # Grid
    GRID_TAB = (By.CSS_SELECTOR, "#demo-tab-grid")
    GRID_ITEMS = (By.CSS_SELECTOR, "#demo-tabpane-grid div[class='list-group-item list-group-item-action']")

class SelectablePageLocators:
    # List
    LIST_ITEMS = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item list-group-item-action']")
    LIST_ACTIVE_ITEMS = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item active list-group-item-action']")

    # Grid
    GRID_TAB = (By.CSS_SELECTOR, "#demo-tab-grid")
    GRID_ITEMS = (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']")
    GRID_ACTIVE_ITEMS = (By.CSS_SELECTOR, "li[class='list-group-item active list-group-item-action']")

class ResizablePageLocators:
    BOX = (By.CSS_SELECTOR, "#resizableBoxWithRestriction")
    HANDLE = (By.CSS_SELECTOR, "span[class='react-resizable-handle react-resizable-handle-se']")

class DroppablePageLocators:
    # Simple
    DRAG = (By.CSS_SELECTOR, "#draggable")
    DROP = (By.CSS_SELECTOR, "#droppable")

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-accept")
    ACCEPTABLE = (By.CSS_SELECTOR, "#acceptable")
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, "#notAcceptable")
    ACCEPRT_DROP = (By.CSS_SELECTOR, "#acceptDropContainer #droppable")

    # Revert
    REVERT_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-revertable")
    REVERTABLE = (By.CSS_SELECTOR, "#revertable")
    NOT_REVERTABLE = (By.CSS_SELECTOR, "#notRevertable")
    REVERT_DROP = (By.CSS_SELECTOR, "#revertableDropContainer #droppable")

class DragabblePageLocators:
    # Simple
    DRAG = (By.CSS_SELECTOR, "#dragBox")

    # Axis
    AXIS_TAB = (By.CSS_SELECTOR, "#draggableExample-tab-axisRestriction")
    ONLY_X = (By.CSS_SELECTOR, "#restrictedX")
    ONLY_Y = (By.CSS_SELECTOR, "#restrictedY")




