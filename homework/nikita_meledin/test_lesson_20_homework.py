import requests
import pytest


@pytest.fixture
def new_post_id():
    body = {
        "name": "Test Object",
        "data": {
            "color": "red",
            "size": "medium"
        }
    }
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body
    )
    post_id = response.json()["id"]
    yield post_id
    print('\nDelete post', post_id)
    requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")


@pytest.fixture(scope="session", autouse=True)
def message():
    print('\nStart testing')
    yield
    print('Testing completed')


@pytest.fixture(scope="function", autouse=True)
def before_after():
    print("\n" + "-" * 30)
    print('before test')
    yield
    print('\nafter test')
    print("-" * 30 + "\n")


def test_get_all_object():
    response = requests.get("http://objapi.course.qa-practice.com/object")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_object_id(new_post_id):
    response = requests.get(f"http://objapi.course.qa-practice.com/object/{new_post_id}")
    assert response.status_code == 200
    assert response.json()['id'] == new_post_id


@pytest.mark.critical
@pytest.mark.parametrize('name, color, size', [
    ('one', 'red', ''),
    ('two', 123, '!@$!$#@%@'),
    ('three', 'blue', True)
])
def test_post_object(name, color, size):
    body = {
        "name": name,
        "data": {
            "color": color,
            "size": size
        }
    }
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    response_body = response.json()
    response_body.pop('id')
    assert response_body == body
    requests.delete(f"http://objapi.course.qa-practice.com/object/{response.json()['id']}")


@pytest.mark.medium
def test_put_object(new_post_id):
    body = {
        "name": "Test Object",
        "data": {
            "color": "green",
            "size": "medium"
        }
    }
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{new_post_id}",
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    response_data = response.json()
    response_data.pop('id')
    assert response_data == body


def test_patch_object(new_post_id):
    body = {"name": "qwe"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{new_post_id}",
        json=body
    )
    assert response.status_code == 200, 'Status code is incorrect'
    response_data = response.json()
    assert response_data["name"] == "qwe"
    assert response_data["id"] == new_post_id


def test_delete_object(new_post_id):
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{new_post_id}")
    assert response.status_code == 200, 'Status code is incorrect'
    expected_message = f"Object with id {new_post_id} successfully deleted"
    assert response.text == expected_message
    get_response = requests.get(f"http://objapi.course.qa-practice.com/object/{new_post_id}")
    assert get_response.status_code == 404, 'Object should not exist'
