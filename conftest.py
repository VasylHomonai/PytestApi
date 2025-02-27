import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

@pytest.fixture
def object_id():
    new_object_endpoint = CreateObject()
    payload = new_object_endpoint.load_json("tests/data/payload.json")  # Виклик методу load_json з батьківського класу
    new_object_endpoint.new_object(payload)
    yield new_object_endpoint.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(new_object_endpoint.response_json['id'])