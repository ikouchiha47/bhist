import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as waitfor
from selenium.webdriver.support import expected_conditions as EC

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


class Crawler:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def quit(self):
        self.driver.quit()

    def scrape(self, url):
        driver = self.driver
        driver.get(url)

        try:
            (
            waitfor(driver, 2)
            .until(wait_for_js_load("return document.readyState", ["complete", "COMPLETE"]))
            )
        finally:
            return driver.title
