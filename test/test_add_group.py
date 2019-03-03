from sys import maxsize
from model.group import Group


def test_group_create_empty_values(app):
    group = Group("", "", "")
    group_list_at_start = app.group.get_list()
    app.group.create(group)
    group_list_after_creation = app.group.get_list()
    assert len(group_list_at_start) + 1 == len(group_list_after_creation)
    expected_group_list = group_list_at_start.copy()
    expected_group_list.append(group)

    assert sorted(expected_group_list, key=Group.id_with_none) == sorted(group_list_after_creation, key=Group.id_with_none)


def test_group_create(app):
    group = Group("Some text 01", "Some text 02", "some text 03")
    group_list_at_start = app.group.get_list()
    app.group.create(group)
    group_list_after_creation = app.group.get_list()
    assert len(group_list_at_start) + 1 == len(group_list_after_creation)
    expected_group_list = group_list_at_start.copy()
    expected_group_list.append(group)

    assert sorted(expected_group_list, key=Group.id_with_none) == sorted(group_list_after_creation, key=Group.id_with_none)
