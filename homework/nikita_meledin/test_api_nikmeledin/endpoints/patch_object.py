import allure
import requests
from test_api_nikmeledin.endpoints.base_endpoint import BaseEndpoint


class PatchObject(BaseEndpoint):

    @allure.step('Sending PATCH request to partially update object')
    def patch_object(self, object_id, payload):
        self.response = requests.patch(f'{self.url}/{object_id}', json=payload)
        self.json = self.response.json()
        return self.json

    @allure.step('Checking that object was partially updated')
    def check_patch_object(self, expected_payload):
        self.check_response_matches_payload(expected_payload)
