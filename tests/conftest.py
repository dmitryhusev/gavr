from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from .utils.main import Page
import allure
from allure_commons.types import AttachmentType


def make_attachment(browser):
    allure.attach(browser.get_screenshot_as_png(), 'screenshot', AttachmentType.PNG)
    allure.attach(browser.current_url, 'url', AttachmentType.TEXT)

chrome_options = Options()
chrome_options.add_argument('--headless')

@pytest.fixture
def action():
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    yield Page(browser)
    make_attachment(browser)
    browser.quit()