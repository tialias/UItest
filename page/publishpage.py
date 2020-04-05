from common.basepage import BasePage
from selenium.webdriver.common.by import By


class PublishPage(BasePage):
    single_line_text_loc = ("xpath", "//input[@value='']")
    multi_line_text_loc = ("xpath", "//textarea")
    radio_loc = ('xpath', "//input[@value='eBnj']")
    checkbox1_loc = ('xpath', "//input[@value='5RnB']")
    checkbox2_loc = ('xpath', "//input[@value='MceL']")
    image_radio_loc = ('xpath', "//input[@value='E3J3']")
    image_checkbox1_loc = ('xpath', "//input[@value='qNda']")
    image_checkbox2_loc = ('xpath', "//input[@value='bl4u']")
    next_page_loc = ('xpath', "//button[@type='button']")
    dropdown_display_loc = ('xpath', "//span/div/div/div/div/div")
    dropdown_value_loc = ('id', "react-select-2-option-1")
    multi_dropdown_display1_loc = ('xpath', '//span/div/div/div/div/div/div/div')
    multi_dropdown_value1_loc = ('id', "react-select-3-option-0")
    multi_dropdown_display2_loc = ('xpath', "//span/div/div/div[2]/div/div/div/div")
    multi_dropdown_value2_loc = ('id', "react-select-4-option-0")
    number_loc = ('xpath', "(//input[@value=''])[4]")
    time_display_loc = ('xpath', "(//input[@value=''])[5]")
    time_value_loc = ('link text', "此刻")
    address_net_loc = ('xpath', "(//input[@value=''])[5]")
    get_location_loc = ('xpath', "(//button[@type='button'])[2]")
    image_goods1_loc = ('xpath', "(//button[@type='button'])[6]")
    image_goods2_loc = ('xpath', "(//button[@type='button'])[8]")
    goods1_loc = ('xpath', "(//button[@type='button'])[16]")
    goods2_loc = ('xpath', "(//button[@type='button'])[18]")
    name_loc = ('xpath', "(//input[@value=''])[5]")
    mob_phone_num_loc = ('xpath', "(//input[@value=''])[5]")
    email_loc = ('xpath', "(//input[@value=''])[5]")
    phone_num_loc = ('xpath', "(//input[@value=''])[5]")
    submit_loc = ('xpath', "(//button[@type='button'])[38]")

    def __init__(self, driver, page_url):
        BasePage.__init__(self, driver, page_url)

    def open_page(self):
        self._open(self.base_url)

    def input_text(self):
        self.send_keys(*self.single_line_text_loc, value="这是单行文字")

    def input_textarea(self):
        self.send_keys(*self.multi_line_text_loc, value="这是多行文字")

    def input_radio(self):
        self.find_element(*self.radio_loc).click()

    def input_checkbox(self):
        self.find_element(*self.checkbox1_loc).click()
        self.find_element(*self.checkbox2_loc).click()

    def input_image_radio(self):
        self.find_element(*self.image_radio_loc).click()

    def input_image_checkbox(self):
        self.find_element(*self.image_checkbox1_loc).click()
        self.find_element(*self.image_checkbox2_loc).click()

    def input_next_page(self):
        self.find_element(*self.next_page_loc).click()

    def input_dropdown(self):
        self.find_element(*self.dropdown_display_loc).click()
        self.find_element(*self.dropdown_value_loc).click()

    def input_multi_dropdown(self):
        self.find_element(*self.multi_dropdown_display1_loc).click()
        self.find_element(*self.multi_dropdown_value1_loc).click()
        self.find_element(*self.multi_dropdown_display2_loc).click()
        self.find_element(*self.multi_dropdown_value2_loc).click()

    def input_number(self):
        self.send_keys(*self.number_loc, value=133)

    def input_time(self):
        self.find_element(*self.time_display_loc).click()
        self.find_element(*self.time_value_loc).click()

    def input_address_net(self):
        self.send_keys(*self.address_net_loc, value="http://jinshuju.net")

    def input_get_location(self):
        self.find_element(*self.get_location_loc).click()

    def input_image_goods(self):
        self.find_element(*self.image_goods1_loc).click()
        self.find_element(*self.image_goods2_loc).click()

    def input_goods(self):
        self.find_element(*self.goods1_loc).click()
        self.find_element(*self.goods2_loc).click()

    def input_user_info(self):
        self.send_keys(self.name_loc, value="张三")
        self.send_keys(self.mob_phone_num_loc, value="13500000000")
        self.send_keys(self.email_loc, value="tedtian@163.com")
        self.send_keys(self.phone_num_loc, value="13500000000")

    def input_submit(self):
        self.find_element(*self.submit_loc).click()
