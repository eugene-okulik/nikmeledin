import allure
import requests
from test_api_nikmeledin.endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    @allure.step('Delete object')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response

    @allure.step('Checking that the object has been deleted')
    def check_delete_object(self, object_id):
        response = requests.get(f'{self.url}/{object_id}')
        assert response.status_code == 404
