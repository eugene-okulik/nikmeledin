import requests
import allure

class BaseEndpoint():
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None


    @allure.step('Sending GET request to fetch all objects')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.json


    @allure.step('Checking response status code')
    def check_status_code(self):
        assert self.response.status_code == 200


    @allure.step('Checking that JSON is present in the response')
    def check_json(self):
        assert self.json is not None







