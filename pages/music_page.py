import time
from .base_page import BasePage
from .locators import MusicPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MusicPage(BasePage):
    def search_music(self, name: str):
        search = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MusicPageLocators.SEARCH))
        search.click()
        search.send_keys(name[:len(name) // 2])
        time.sleep(1)
        popup_list = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(MusicPageLocators.POPUP_LIST))
        '''popup_list_items = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(MusicPageLocators.POPUP_LIST_ITEMS))'''
        popup_list_items = self.driver.find_elements(*MusicPageLocators.POPUP_LIST_ITEMS)
        for item in popup_list_items:
            if item.text == name:
                action = ActionChains(self.driver).move_to_element(item).click().perform()

    def get_artist_title(self):
        artist_title = self.driver.find_element(*MusicPageLocators.ARTIST_TITLE).text
        return artist_title

    def get_first_top_album_artist_title(self):
        first_top_album_artist_title = self.driver.find_element(*MusicPageLocators.FIRST_TOP_ALBUM_TITLE).text
        return first_top_album_artist_title

    def get_last_top_album_artist_title(self):
        last_top_album_artist_title = self.driver.find_element(*MusicPageLocators.LAST_TOP_ALBUM_TITLE).text
        return last_top_album_artist_title

    def click_first_top_song(self):
        first_top_song = self.driver.find_element(*MusicPageLocators.FIRST_TOP_SONG)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", first_top_song)
        move_mouse_on = ActionChains(self.driver).move_to_element(first_top_song)
        move_mouse_on.click()
        move_mouse_on.perform()

    def check_play_or_pause(self):
        shortcut_icon = self.driver.find_element(*MusicPageLocators.SHORTCUT_ICON)
        status = shortcut_icon.get_attribute('href')
        if 'pause' in status:
            return 'pause'
        elif 'play' in status:
            return 'play'


