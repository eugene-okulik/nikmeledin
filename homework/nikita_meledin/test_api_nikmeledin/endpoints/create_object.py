import requests
import allure

from test_api_nikmeledin.endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):

    @allure.step('Creating a new object')
    def create_new_object(self, payload):
        self.response = requests.post(self.url, json=payload)
        self.json = self.response.json()
        self.json_response = self.response.json()
        return self.json_response['id']


    @allure.step('Checking that created object (without id) matches expected')
    def check_created_object_matches(self, payload):
        response_without_id = self.json_response.copy()
        response_without_id.pop('id')
        assert response_without_id == payload
