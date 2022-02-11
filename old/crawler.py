import os

from urllib.parse import urlparse, ParseResult
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as waitfor
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

os.environ['MOZ_HEADLESS'] = '1'

class wait_for_js_load(object):
    def __init__(self, execute_str, expected_values):
        self.expected_values = expected_values
        self.execute_str = execute_str

    def __call__(self, driver):
        try:
            v = driver.execute_script(self.execute_str)
            return str(v) in self.expected_values
        except StaleElementReferenceException:
            return False

class Webpage:
    def __init__(self, url, title, body):
        self.url: ParseResult  = self.__make_url__(url)
        self.title: str = title
        self.body: str = body

    def __make_url__(self, url):
        url = url.strip()
        if not url.startswith('http:') or not url.startswith('https:') or not url.startswith('//'):
            url = "//" + url

        return urlparse(url)

class Crawler:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def quit(self):
        self.driver.quit()

    def scrape(self, url) -> Webpage:
        driver = self.driver
        driver.get(url)

        try:
            (
            waitfor(driver, 2)
            .until(wait_for_js_load("return document.readyState", ["complete", "COMPLETE"]))
            )
        finally:
            # return driver.title
            body = driver.find_element_by_tag_name("body").text
            return Webpage(url, driver.title, body)

