from common.basepage import BasePage
from selenium.webdriver.common import by


class PublishPage(BasePage):
    single_line_text_loc = (by.xpath, "//input[@value='']")
    multi_line_text_loc = (by.xpath, "//textarea")

    def open_page(self, page_url):
        self.open_page(self.page_url)

    def input_text(self):
        self.send_keys(*self.single_line_text_loc, "这是单行文字", True, False)

    def input_textarea(self):
        self.send_keys(*self.multi_line_text_loc, "这是多行文字", True, False)
        
