from model.group import Group


def test_delete_first_group(app):
    if app.group.count() < 1:
        app.group.create(Group("New group name"))
    group_list_at_start = app.group.get_list()
    app.group.delete()
    group_list_after_deletion = app.group.get_list()
    assert len(group_list_at_start) - 1 == len(group_list_after_deletion)
    expected_group_list = group_list_at_start.copy()
    expected_group_list[0:1] = []
    assert group_list_after_deletion == expected_group_list

