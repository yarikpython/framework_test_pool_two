from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import os
import config

firefox_exe_path = os.path.normpath(config.GECKODRIVER_EXE)
chrome_exe_path = os.path.normpath(config.CHROMEDRIVER_EXE)


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument('start-maximized')
    # chrome_options.headless = True
    driver = webdriver.Chrome(executable_path=chrome_exe_path, options=chrome_options)
    yield driver
    driver.quit()
