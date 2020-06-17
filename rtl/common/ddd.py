import requests
from faker import Faker
from locust import Locust, TaskSet, task, User, HttpUser

from rtl.common.conf import Choujiang


class WfTask(TaskSet):
    def on_start(self):
        self.fake = Faker(locale='zh_CN')
        self.client.get(url="https://staging.jinshuju.net/f/DIoQKq")

    def schedule_task(self, Choujiang(), first=False):


class WebsiteUser(HttpUser):
    task_set = WfTasks
    host = "https://staging.jinshuju.net/"
    min_wait = 1000
    max_wait = 5000
