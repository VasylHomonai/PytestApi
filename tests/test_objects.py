from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject


def test_create_object():
        new_object_endpoint = CreateObject()
        payload = new_object_endpoint.load_json("tests/data/payload.json")  # Виклик методу load_json з батьківського класу
        new_object_endpoint.new_object(payload=payload)
        new_object_endpoint.check_response_is_200()
        new_object_endpoint.check_name(payload['name'])
        new_object_endpoint.check_year(payload['data']['year'])
        new_object_endpoint.check_price(payload['data']['price'])
        new_object_endpoint.check_model(payload['data']['CPU model'])
        new_object_endpoint.check_size(payload['data']['Hard disk size'])

        # Видалення створеного об'єкта
        obj_id = new_object_endpoint.response_json["id"]
        delete_object = DeleteObject()
        delete_object.delete_by_id(obj_id)


def test_get_object(object_id):
        get_object_endpoint = GetObject()
        get_object_endpoint.get_by_id(object_id)
        get_object_endpoint.check_response_is_200()
        get_object_endpoint.check_response_id(object_id)


def test_put_object(object_id):
        update_object_endpoint = UpdateObject()
        updated_payload = update_object_endpoint.load_json("tests/data/updated_payload.json")  # Виклик методу load_json з батьківського класу
        update_object_endpoint.update_by_id(object_id, updated_payload)
        update_object_endpoint.check_response_is_200()
        update_object_endpoint.check_response_name(updated_payload['name'])
        update_object_endpoint.check_response_year(updated_payload['data']['year'])
        update_object_endpoint.check_response_price(updated_payload['data']['price'])
        update_object_endpoint.check_response_model(updated_payload['data']['CPU model'])
        update_object_endpoint.check_response_size(updated_payload['data']['Hard disk size'])


def test_del_object(object_id):
        delete_object_endpoint = DeleteObject()
        delete_object_endpoint.delete_by_id(object_id)
        delete_object_endpoint.check_response_is_200()
        get_object_endpoint = GetObject()
        get_object_endpoint.get_by_id(object_id)
        get_object_endpoint.check_response_is_404()
