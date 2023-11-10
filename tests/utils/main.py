from selenium.common import exceptions as exc
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# wd = webdriver.WebDriver()

class Page:

    def __init__(self, browser):
        self.browser = browser

    def element(self, locator):
        el = WebDriverWait(self.browser, 10).until(lambda x: x.find_element(By.XPATH, locator))
        return el

    def click(self, locator):
        self.element(locator).click()

    def navigate(self):
        self.browser.get(url='http://localhost:8000')

    def enter_text(self, locator, text):
        self.element(locator).send_keys(text)

    def element_has_text(self, text):
        return self.element(f'//*[contains(text(), "{text}")]')
