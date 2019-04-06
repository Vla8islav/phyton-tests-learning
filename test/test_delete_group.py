from random import randint

from model.group import Group


def test_delete_group(app, db, check_ui):
    if app.group.count() < 1:
        app.group.create(Group("New group name"))
    index = randint(0, len(db.get_group_list()))
    group_list_at_start = db.get_group_list()
    app.group.delete(index)
    group_list_after_deletion = db.get_group_list()
    assert len(group_list_at_start) - 1 == len(group_list_after_deletion)
    expected_group_list = group_list_at_start.copy()
    expected_group_list[index:index+1] = []
    assert group_list_after_deletion == expected_group_list
    if check_ui:
        assert sorted(expected_group_list, key=Group.id_with_none) == sorted(app.group.get_list(),
                                                                             key=Group.id_with_none)

