import allure
import requests

from test_api_nikmeledin.endpoints.base_endpoint import BaseEndpoint


class PatchObject(BaseEndpoint):

    @allure.step('Sending PATCH request to partially update object')
    def patch_object(self, object_id, payload):
        self.response = requests.patch(f'{self.url}/{object_id}', json=payload)
        return self.response.json()

    @allure.step('Checking that object was partially updated (without id)')
    def check_patch_object(self, expected_payload):
        updated_without_id = self.json.copy()
        updated_without_id.pop('id')
        assert updated_without_id == expected_payload
