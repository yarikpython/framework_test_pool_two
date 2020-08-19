from .base_page import BasePage
from .locators import MarketPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MarketPage(BasePage):
    def search_product(self, product_name: str):
        search = self.driver.find_element(*MarketPageLocators.SEARCH)
        search.send_keys(product_name)
        submit = self.driver.find_element(*MarketPageLocators.SUBMIT)
        submit.click()

    def go_to_product_page(self, how, what):
        item = self.driver.find_element(how, what)
        item.click()

    def get_product_name(self, how, what):
        item = self.driver.find_element(how, what)
        return item.get_attribute('title')

    def go_to_compare_page(self):
        compare_link = self.driver.find_element(*MarketPageLocators.COMPARE_LINK)
        compare_link.click()

    def sort_by_price_fade_out(self):
        sort_by_price_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MarketPageLocators.SORT_BY_PRICE_BUTTON))
        ActionChains(self.driver).double_click(sort_by_price_button).perform()

    def first_price_more_than_second(self):
        first_price = self.driver.find_element(*MarketPageLocators.FIRST_RESULT_ITEM_PRICE).text.replace(' ',
                                                                                                         '').replace(
            ',', '.')
        second_price = self.driver.find_element(*MarketPageLocators.SECOND_RESULT_ITEM_PRICE).text.replace(' ',
                                                                                                           '').replace(
            ',', '.')
        return True if float(first_price) >= float(second_price) else False

    def go_to_appliances(self):
        appliances_link = self.driver.find_element(*MarketPageLocators.APPLIANCES_LINK)
        appliances_link.click()

    def get_width(self, how, what):
        params_with_desc: str = self.driver.find_element(how, what).text
        desc, params = params_with_desc.split(":")
        width, _, _ = params.split('х')
        return float(width)

    def set_width_to(self, width: str):
        input_width = self.driver.find_element(*MarketPageLocators.INPUT_WIDTH_TO)
        input_width.send_keys(width)

    def go_to_fridges(self):
        fridges_link = self.driver.find_element(*MarketPageLocators.FRIDGES_LINK)
        fridges_link.click()

