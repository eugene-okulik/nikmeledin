import pytest

from test_api_nikmeledin.endpoints.base_endpoint import BaseEndpoint
from test_api_nikmeledin.endpoints.create_object import CreateObject
from test_api_nikmeledin.endpoints.delete_object import DeleteObject
from test_api_nikmeledin.endpoints.patch_object import PatchObject
from test_api_nikmeledin.endpoints.update_object import UpdateObject


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
