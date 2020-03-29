import time
import unittest
from page.publishpage import PublishPage
from selenium import webdriver


class CasePublish(unittest.TestCase):
    def setUp(self):
        self.url = "https://tes.uat.jinshuju.net/f/28S5as?force_fe=1"
        self.driver = webdriver.Chrome()

    def testPublish(self):
        publish_page = PublishPage(self.driver, self.url)
        publish_page.open_page()
        publish_page.input_text()
        publish_page.input_textarea()
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
