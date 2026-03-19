from locust import HttpUser, task
import random


EXISTING_IDS = [4985, 5098, 5099, 5164, 5304]

class ObjectUser(HttpUser):
    host = "http://objapi.course.qa-practice.com"

    @task(3)
    def get_one_object(self):
        self.client.get(f"/object/{random.choice(EXISTING_IDS)}")

    @task(1)
    def get_all_objects(self):
        self.client.get("/object")
