import time
from pages.main_page import MainPage
from pages.market_page import MarketPage
from pages.product_page import ProductPage
from pages.compare_page import ComparePage
from pages.music_page import MusicPage
from pages.locators import MarketPageLocators
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType


@allure.feature('Yandex Market')
@allure.story('Поиск товаров, добавление в сравнение')
def test_market_search_and_compare(driver):
    url = 'https://yandex.ru'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_market()
    market_window = driver.window_handles[1]
    driver.switch_to.window(market_window)
    market_page = MarketPage(driver, driver.current_url)
    market_page.search_product('Note 8')
    first_item_name = market_page.get_product_name(*MarketPageLocators.FIRST_RESULT_ITEM)
    market_page.go_to_product_page(*MarketPageLocators.FIRST_RESULT_ITEM)
    product_window = driver.window_handles[2]
    driver.switch_to.window(product_window)
    product_page = ProductPage(driver, driver.current_url)
    product_page.add_to_comparison()
    driver.close()
    driver.switch_to.window(market_window)
    second_item_name = market_page.get_product_name(*MarketPageLocators.SECOND_RESULT_ITEM)
    market_page.go_to_product_page(*MarketPageLocators.SECOND_RESULT_ITEM)
    product_window = driver.window_handles[2]
    driver.switch_to.window(product_window)
    product_page = ProductPage(driver, driver.current_url)
    product_page.add_to_comparison()
    driver.close()
    driver.switch_to.window(market_window)
    market_page.go_to_compare_page()
    compare_page = ComparePage(driver, driver.current_url)
    with allure.step('Screenshot compare page'):
        allure.attach(driver.get_screenshot_as_png(), name='screenshot compare', attachment_type=AttachmentType.PNG)
    assert compare_page.is_element_present(By.XPATH,
                                           f"//a[text() = '{first_item_name}']") and compare_page.is_element_present(
        By.XPATH, f"//a[text() = '{second_item_name}']")


@allure.feature('Yandex Market')
@allure.story('Поиск товаров, добавление в сравнение и удаление')
def test_add_to_compare_and_delete(driver):
    url = 'https://yandex.ru'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_market()
    market_window = driver.window_handles[1]
    driver.switch_to.window(market_window)
    market_page = MarketPage(driver, driver.current_url)
    market_page.search_product('Note 8')
    first_item_name = market_page.get_product_name(*MarketPageLocators.FIRST_RESULT_ITEM)
    market_page.go_to_product_page(*MarketPageLocators.FIRST_RESULT_ITEM)
    product_window = driver.window_handles[2]
    driver.switch_to.window(product_window)
    product_page = ProductPage(driver, driver.current_url)
    product_page.add_to_comparison()
    driver.close()
    driver.switch_to.window(market_window)
    second_item_name = market_page.get_product_name(*MarketPageLocators.SECOND_RESULT_ITEM)
    market_page.go_to_product_page(*MarketPageLocators.SECOND_RESULT_ITEM)
    product_window = driver.window_handles[2]
    driver.switch_to.window(product_window)
    product_page = ProductPage(driver, driver.current_url)
    product_page.add_to_comparison()
    driver.close()
    driver.switch_to.window(market_window)
    market_page.go_to_compare_page()
    compare_page = ComparePage(driver, driver.current_url)
    assert compare_page.is_element_present(By.XPATH,
                                           f"//a[text() = '{first_item_name}']") and compare_page.is_element_present(
        By.XPATH, f"//a[text() = '{second_item_name}']")
    compare_page.delete_list()
    with allure.step('Screenshot compare page without products'):
        allure.attach(driver.get_screenshot_as_png(), name='screenshot nothing to compare',
                      attachment_type=AttachmentType.PNG)
    assert compare_page.is_element_present(By.XPATH, "//h2[text()='Сравнивать пока нечего']")


@allure.feature('Yandex Market')
@allure.story('Сортировка по цене')
def test_sort_by_price(driver):
    url = 'https://yandex.ru'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_market()
    market_window = driver.window_handles[1]
    driver.switch_to.window(market_window)
    market_page = MarketPage(driver, driver.current_url)
    market_page.search_product('экшн-камеры')
    market_page.sort_by_price_fade_out()
    time.sleep(1)
    assert market_page.first_price_more_than_second()


@allure.feature('Yandex Market')
@allure.story('Сортировка по параметрам(Ширина)')
def test_sort_fridges_by_width(driver):
    url = 'https://yandex.by'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_market()
    market_window = driver.window_handles[1]
    driver.switch_to.window(market_window)
    market_page = MarketPage(driver, driver.current_url)
    market_page.go_to_appliances()
    appliance_page = MarketPage(driver, driver.current_url)
    appliance_page.go_to_fridges()
    market_page_fridges = MarketPage(driver, driver.current_url)
    market_page_fridges.set_width_to('50')
    market_page_sorted_fridges = MarketPage(driver, driver.current_url)
    time.sleep(5)
    assert market_page_sorted_fridges.get_width(
        *MarketPageLocators.PARAMS_FIRST_ITEM) <= 50 and market_page_sorted_fridges.get_width(
        *MarketPageLocators.PARAMS_LAST_ITEM) <= 50


@allure.feature('Yandex Music')
@allure.story('Поиск музыки')
def test_search_music(driver):
    url = 'https://yandex.by'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_music()
    music_window = driver.window_handles[1]
    driver.switch_to.window(music_window)
    music_page = MusicPage(driver, driver.current_url)
    music_page.search_music('Metallica')
    music_page = MusicPage(driver, driver.current_url)
    with allure.step('Screenshot page after search'):
        allure.attach(driver.get_screenshot_as_png(), name='scrnst after search', attachment_type=AttachmentType.PNG)
    assert music_page.get_artist_title() == 'Metallica'
    assert music_page.get_first_top_album_artist_title() == 'Metallica'
    assert music_page.get_last_top_album_artist_title() == 'Metallica'


@allure.feature('Yandex Music')
@allure.story('Поиск музыки и воспроизведение и пауза')
def test_play_top_song(driver):
    url = 'https://yandex.by'
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.go_to_music()
    music_window = driver.window_handles[1]
    driver.switch_to.window(music_window)
    music_page = MusicPage(driver, driver.current_url)
    music_page.search_music('Beyoncé')
    music_page = MusicPage(driver, driver.current_url)
    music_page.click_first_top_song()
    assert music_page.check_play_or_pause() == 'play'
    music_page.click_first_top_song()
    assert music_page.check_play_or_pause() == 'pause'
