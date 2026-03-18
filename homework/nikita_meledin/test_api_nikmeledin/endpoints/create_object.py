import requests
import allure
from test_api_nikmeledin.endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):

    @allure.step('Creating a new object')
    def create_new_object(self, payload):
        self.response = requests.post(self.url, json=payload)
        self.json = self.response.json()
        return self.json['id']
