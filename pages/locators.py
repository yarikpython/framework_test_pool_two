from selenium.webdriver.common.by import By


class MainPageLocators:
    NAV_LINK_MARKET = (By.CSS_SELECTOR, '[data-id="market"]')
    NAV_LINK_MARKET_V2 = (By.XPATH, "//div[contains(text(), 'Маркет')]")
    NAV_LINK_MUSIC = (By.CSS_SELECTOR, '[data-id="music"]')
    NAV_LINK_MUSIC_V2 = (By.XPATH, "//div[contains(text(), 'Музыка')]")


class MarketPageLocators:
    SEARCH = (By.ID, 'header-search')
    SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')
    FIRST_RESULT_ITEM = (
        By.CSS_SELECTOR, "[data-zone-name='snippetList']>article:nth-child(1)>div>h3[data-zone-name='title']>a")
    SECOND_RESULT_ITEM = (
        By.CSS_SELECTOR, "[data-zone-name='snippetList']>article:nth-child(2)>div>h3[data-zone-name='title']>a")
    COMPARE_LINK = (By.CSS_SELECTOR, 'div[data-apiary-widget-id="/content/header/compareButton"]')
    SORT_BY_PRICE_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-id='dprice']")
    FIRST_RESULT_ITEM_PRICE = (
        By.CSS_SELECTOR,
        "[data-zone-name='snippetList']>article:nth-child(1) [data-zone-name='price'] span>span:first-child")
    SECOND_RESULT_ITEM_PRICE = (
        By.CSS_SELECTOR,
        "[data-zone-name='snippetList']>article:nth-child(2) [data-zone-name='price'] span>span:first-child")
    APPLIANCES_LINK = (By.XPATH, "//span[text()='Бытовая техника']/parent::a")
    INPUT_WIDTH_TO = (By.CSS_SELECTOR, "input[name='Ширина до']")
    PARAMS_FIRST_ITEM = (By.XPATH, "//div[@data-zone-name='snippetList']/article[1]//li[contains(text(),'ШхВхГ')]")
    PARAMS_LAST_ITEM = (By.XPATH, "//div[@data-zone-name='snippetList']/article[last()]//li[contains(text(),'ШхВхГ')]")
    FRIDGES_LINK = (By.XPATH, "//a[text()='Холодильники']")


class ProductPageLocators:
    COMPARE = (By.XPATH, "//span[contains(text(), 'Сравнить')]/parent::div")


class ComparePageLocators:
    DELETE_LIST = (By.CSS_SELECTOR, "div[data-apiary-widget-id='/content/compareContent/compareToolbar']>div>button")


class MusicPageLocators:
    SEARCH = (By.CSS_SELECTOR, ".head__search input")
    ARTIST_TITLE = (By.CSS_SELECTOR, "h1.page-artist__title")
    FIRST_TOP_ALBUM_TITLE = (By.CSS_SELECTOR, "div[data-card='top_albums']>div:first-child>div.album__artist")
    LAST_TOP_ALBUM_TITLE = (By.CSS_SELECTOR, "div[data-card='top_albums']>div:last-child>div.album__artist")
    POPUP_LIST = (By.CLASS_NAME, 'd-suggest__entities')
    POPUP_LIST_ITEMS = (By.CLASS_NAME, 'd-suggest-item__title-main')
    FIRST_TOP_SONG = (By.CSS_SELECTOR, '.page-artist__tracks_top>div:first-child>.d-track__start-column')
    SHORTCUT_ICON = (By.CSS_SELECTOR, "[rel='shortcut icon']")
