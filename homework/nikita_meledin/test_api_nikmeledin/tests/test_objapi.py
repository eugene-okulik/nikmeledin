import pytest

payload = {"data": {"color": "color", "size": "size"}, "name": "name"}
new_payload = {"name": 'name2', "data": {"color": 'color2', "size": 'size2'}}
patch_payload = {"name": "test"}


def test_get_all_object(get_all_objects):
    get_all_objects.get_all_objects()
    get_all_objects.check_status_code()
    get_all_objects.check_json()


def test_post_object(create_new_object, delete_object):
    object_id = create_new_object.create_new_object(payload)
    create_new_object.check_status_code()
    delete_object.delete_object(object_id)
    delete_object.check_delete_object(object_id)


def test_put_object(create_new_object, update_object):
    object_id = create_new_object.create_new_object(payload)
    create_new_object.check_status_code()
    update_object.update_object(object_id, new_payload)
    update_object.check_json()
    update_object.check_updated_object(new_payload)


def test_patch_object(create_new_object, patch_object):
    object_id = create_new_object.create_new_object(payload)
    create_new_object.check_status_code()
    patch_object.patch_object(object_id, patch_payload)


def test_delete_object(delete_object, create_new_object):
    object_id = create_new_object.create_new_object(payload)
    create_new_object.check_status_code()
    delete_object.delete_object(object_id)
    delete_object.check_delete_object(object_id)
