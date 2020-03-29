from common.basepage import BasePage
from selenium.webdriver.common.by import By


class PublishPage(BasePage):
    single_line_text_loc = ("xpath", "//input[@value='']")
    multi_line_text_loc = ("xpath", "//textarea")

    def __init__(self, driver, page_url):
        BasePage.__init__(self, driver, page_url)

    def open_page(self):
        self._open(self.base_url)

    def input_text(self):
        self.page_send_keys(*self.single_line_text_loc, value="这是单行文字")

    def input_textarea(self):
        self.page_send_keys(*self.multi_line_text_loc, value="这是多行文字")
