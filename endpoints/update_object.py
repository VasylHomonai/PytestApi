import requests
from endpoints.base_endpoint import Endpoint

class UpdateObject(Endpoint):

    def update_by_id(self, object_id, updated_payload):
        self.response = requests.put(self.get_full_url(object_id), json=updated_payload)
        self.response_json = self.response.json()

    def check_response_name(self, name):
        assert self.response_json['name'] == name

    def check_response_year(self, year):
        assert self.response_json['data']['year'] == year

    def check_response_price(self, price):
        assert self.response_json['data']['price'] == price

    def check_response_model(self, model):
        assert self.response_json['data']['CPU model'] == model

    def check_response_size(self, size):
        assert self.response_json['data']['Hard disk size'] == size