"""
BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url, base_title):
        self.driver = driver
        self.base_url = base_url
        self.base_title = base_title

    def _open(self, page_url):
        self.driver.get(page_url)

    def open_page(self):
        self._open(self.base_url)

    def find_element(self, *locator):
        # 重写元素定位
        try:
            WebDriverWait.until(self.driver, 10).until(EC.presence_of_element_located(locator))
        except Exception as msg:
            print("%s页面未找到%s元素" % (self, locator))

    def send_keys(self, loc, value, first_click=True, first_clear=True):
        try:
            loc = getattr(self, "_%s"(loc))
            if first_click:
                self.find_element(*loc).click()
            if first_clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))
