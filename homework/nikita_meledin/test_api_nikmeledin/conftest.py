import pytest
from test_api_nikmeledin.endpoints.base_endpoint import BaseEndpoint
from test_api_nikmeledin.endpoints.create_object import CreateObject
from test_api_nikmeledin.endpoints.delete_object import DeleteObject
from test_api_nikmeledin.endpoints.patch_object import PatchObject
from test_api_nikmeledin.endpoints.update_object import UpdateObject


@pytest.fixture
def payload():
    return {"data": {"color": "color", "size": "size"}, "name": "name"}


@pytest.fixture
def new_payload():
    return {"name": "name2", "data": {"color": "color2", "size": "size2"}}


@pytest.fixture
def patch_payload():
    return {"name": "test"}


@pytest.fixture
def get_all_objects():
    return BaseEndpoint()


@pytest.fixture
def create_new_object():
    return CreateObject()


@pytest.fixture
def update_object():
    return UpdateObject()


@pytest.fixture
def patch_object():
    return PatchObject()


@pytest.fixture
def delete_object():
    return DeleteObject()


@pytest.fixture
def created_and_delete_object(create_new_object, delete_object, payload):
    object_id = create_new_object.create_new_object(payload)
    create_new_object.check_status_code()
    yield object_id
    delete_object.delete_object(object_id)


@pytest.fixture
def created_object(create_new_object, payload):
    object_id = create_new_object.create_new_object(payload)
    create_new_object.check_status_code()
    return object_id
