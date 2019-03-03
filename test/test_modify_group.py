from model.group import Group
from model.user import User


def test_group_modify_first_group(app):
    if app.group.count() < 1:
        app.group.create(Group("New group name"))
    group = Group("New value1", "val2", "val3")
    app.group.modify_group(group)
    group_list_at_start = app.group.get_list()
    app.group.modify_group(group)
    group_list_after_creation = app.group.get_list()
    assert len(group_list_at_start) == len(group_list_after_creation)


def test_group_modify_first_group_name_only(app):
    if app.group.count() < 1:
        app.group.create(Group("New group name"))
    group = Group("New value1_name_only")
    group_list_at_start = app.group.get_list()
    app.group.modify_group(group)
    group_list_after_creation = app.group.get_list()
    assert len(group_list_at_start) == len(group_list_after_creation)

