import requests
from endpoints.base_endpoint import Endpoint

class DeleteObject(Endpoint):

    def delete_by_id(self, object_id):
        self.response = requests.delete(self.get_full_url(object_id))
        self.response_json = self.response.json()
