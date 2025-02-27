from enum import nonmember
from http.client import responses

import requests
from endpoints.base_endpoint import Endpoint

class CreateObject(Endpoint):

    def new_object(self, payload):
        self.response = requests.post(self.base_url, json=payload)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name

    def check_year(self, year):
        assert self.response_json['data']['year'] == year

    def check_price(self, price):
        assert self.response_json['data']['price'] == price

    def check_model(self, model):
        assert self.response_json['data']['CPU model'] == model

    def check_size(self, size):
        assert self.response_json['data']['Hard disk size'] == size