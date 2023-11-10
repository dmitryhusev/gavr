from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from .utils.main import Page


chrome_options = Options()
chrome_options.add_argument('--headless')

@pytest.fixture
def action():
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    yield Page(browser)
    browser.quit()