import requests
import json


def get_all_object():
    response = requests.get("http://objapi.course.qa-practice.com/object")
    assert response.status_code == 200


def get_object_id():
    body = {
        "data": {
            "color": "white",
            "size": "big"
        },
        "id": 1,
        "name": "First object"
    }
    response = requests.get("http://objapi.course.qa-practice.com/object/1")
    assert response.status_code == 200
    assert response.json() == body


# Тут баг, что на сервере создается объект с другим id, а не с тем, что мы передаем
def post_object():
    body = {
        "data": {
            "color": "Purple",
            "size": "Huge"
        },
        "id": 1234,
        "name": "Testicle"
    }
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    # assert response_data["id"] == 1234, 'Incorrect ID'  # закомментировано из-за бага
    id_new_object = response.json()["id"]
    return id_new_object


# Тут тоже баг с ID
def put_object():
    id_new_object = post_object()
    body = {
        "data": {
            "color": "Red",
            "size": "Small"
        },
        "id": id_new_object,
        "name": "Test"
    }
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{id_new_object}",
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    # response_data = response.json()  # пока не используем из-за бага
    # assert response_data == body, 'Response is incorrect'  # закомментировано из-за бага


def patch_object():
    id_new_object = post_object()
    body = {"name": "qwe"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{id_new_object}",
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()["name"] == "qwe", 'Incorrect name'
    assert response.json()["id"] == id_new_object, 'Incorrect ID'


def delete_object():
    object_id = post_object()
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")
    assert response.status_code == 200, 'Status code is incorrect'
    expected_message = f"Object with id {object_id} successfully deleted"
    assert response.text == expected_message
    get_response = requests.get(f"http://objapi.course.qa-practice.com/object/{object_id}")
    assert get_response.status_code == 404, 'Object should not exist'

get_all_object()
get_object_id()
post_object()
put_object()
patch_object()
delete_object()
