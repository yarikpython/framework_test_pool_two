from .base_page import BasePage
from .locators import ComparePageLocators


class ComparePage(BasePage):
    def delete_list(self):
        delete_button = self.driver.find_element(*ComparePageLocators.DELETE_LIST)
        delete_button.click()