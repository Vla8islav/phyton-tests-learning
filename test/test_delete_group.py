from model.group import Group


def test_delete_first_group(app):
    if app.group.count() < 1:
        app.group.create(Group("New group name"))
    group_list_at_start = app.group.get_list()
    app.group.delete()
    group_list_after_creation = app.group.get_list()
    assert len(group_list_at_start) - 1 == len(group_list_after_creation)
