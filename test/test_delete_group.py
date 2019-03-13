from random import randint

from model.group import Group


def test_delete_group(app):
    if app.group.count() < 1:
        app.group.create(Group("New group name"))
    index = randint(0, app.group.count()-1)
    group_list_at_start = app.group.get_list()
    app.group.delete(index)
    assert len(group_list_at_start) - 1 == app.group.count()
    group_list_after_deletion = app.group.get_list()
    expected_group_list = group_list_at_start.copy()
    expected_group_list[index:index+1] = []
    assert group_list_after_deletion == expected_group_list

