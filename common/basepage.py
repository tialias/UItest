"""
BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
"""


class BasePage():
    def __init__(self, driver, base_url, base_title):
        self.driver = driver
        self.base_url = base_url
        self.base_title = base_title
    def open_page(self):

