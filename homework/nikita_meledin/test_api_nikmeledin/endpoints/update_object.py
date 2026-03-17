import requests
import allure
from test_api_nikmeledin.endpoints.base_endpoint import BaseEndpoint


class UpdateObject(BaseEndpoint):

    @allure.step('Updating created object')
    def update_object(self, object_id, payload):
        self.response = requests.put(f'{self.url}/{object_id}', json=payload)
        if self.response.status_code == 200:
            self.json = self.response.json()
        else:
            self.json = None
        return self.response

    @allure.step('Check status code after update')
    def check_status_code_after_update(self):
        assert self.response.status_code == 200
