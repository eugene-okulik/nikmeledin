import pytest


def test_get_all_object(get_all_objects):
    get_all_objects.get_all_objects()
    get_all_objects.check_status_code()
    get_all_objects.check_json()


def test_post_object(create_new_object, delete_object, payload):
    object_id = create_new_object.create_new_object(payload)
    create_new_object.check_status_code()
    delete_object.delete_object(object_id)
    delete_object.check_delete_object(object_id)


def test_put_object(update_object, created_and_delete_object, new_payload):
    update_object.update_object(created_and_delete_object, new_payload)
    update_object.check_status_code()
    update_object.check_json()
    update_object.check_updated_object(new_payload)


def test_patch_object(patch_object, created_and_delete_object, patch_payload):
    patch_object.patch_object(created_and_delete_object, patch_payload)
    patch_object.check_status_code()


def test_delete_object(delete_object, created_object):
    delete_object.delete_object(created_object)
    delete_object.check_delete_object(created_object)
