import time
import unittest
from page.publishpage import PublishPage
from selenium import webdriver


class CasePublish(unittest.TestCase):
    def setUp(self):
        self.url = "https://tes.uat.jinshuju.net/f/28S5as?force_fe=1"
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()

    def testPublish(self):
        publish_page = PublishPage(self.driver, self.url)
        publish_page.open_page()
        publish_page.input_text()
        publish_page.input_textarea()
        publish_page.input_radio()
        publish_page.input_checkbox()
        publish_page.input_image_radio()
        publish_page.input_image_checkbox()
        publish_page.input_next_page()
        publish_page.input_dropdown()
        publish_page.input_multi_dropdown()
        publish_page.input_time()
        publish_page.input_address_net()
        publish_page.input_get_location()
        publish_page.input_image_goods()
        publish_page.input_goods()
        publish_page.input_user_info()
        publish_page.input_submit()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
