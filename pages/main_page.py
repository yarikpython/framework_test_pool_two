from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):
    def go_to_market(self):
        try:
            nav_link_market = self.driver.find_element(*MainPageLocators.NAV_LINK_MARKET)
            nav_link_market.click()
        except NoSuchElementException:
            nav_link_market = self.driver.find_element(*MainPageLocators.NAV_LINK_MARKET_V2)
            nav_link_market.click()

    def go_to_music(self):
        try:
            nav_link_market = self.driver.find_element(*MainPageLocators.NAV_LINK_MUSIC)
            nav_link_market.click()
        except NoSuchElementException:
            nav_link_market = self.driver.find_element(*MainPageLocators.NAV_LINK_MUSIC_V2)
            nav_link_market.click()
