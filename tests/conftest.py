from selenium import webdriver
import pytest
from .utils.main import Page

@pytest.fixture
def action():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield Page(browser)
    browser.quit()