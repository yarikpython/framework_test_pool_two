from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_comparison(self):
        compare = self.driver.find_element(*ProductPageLocators.COMPARE)
        compare.click()
