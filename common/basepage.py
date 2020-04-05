"""
BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
"""
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def _open(self, base_url):
        self.driver.get(base_url)

    # def open_page(self):
    #     self._open(self.base_url)

    def find_element(self, *locator):
        # 重写元素定位
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*locator)
            )
            return self.driver.find_element(*locator)
        except Exception as e:
            print("%s页面未找到%s元素" % (self, locator))

    def send_keys(self, *loc, value, first_click=True, first_clear=True):
        try:
            # loc = getattr(self, "_%s" % loc)
            if first_click:
                self.find_element(*loc).click()
            if first_clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))

