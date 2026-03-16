import requests
import allure


class BaseEndpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None

    @allure.step('Sending GET request to fetch all objects')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.json

    @allure.step('Checking response status code')
    def check_status_code(self, expected_code=200):
        assert self.response.status_code == expected_code

    @allure.step('Checking that JSON is present in the response')
    def check_json(self):
        assert self.json is not None

    @allure.step('Checking that response body (without id) matches expected payload')
    def check_response_matches_payload(self, expected_payload):
        response_without_id = self.json.copy()
        response_without_id.pop('id', None)
        assert response_without_id == expected_payload
