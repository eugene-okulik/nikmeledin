import requests
import allure
from test_api_nikmeledin.endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):

    @allure.step('Creating a new object')
    def create_new_object(self, payload):
        self.response = requests.post(self.url, json=payload)
        self.json = self.response.json()
        return self.json['id']

    @allure.step('Checking that created object matches expected payload')
    def check_created_object_matches(self, payload):
        self.check_response_matches_payload(payload)
