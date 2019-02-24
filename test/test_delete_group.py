from model.group import Group


def test_delete_first_group(app):
    if app.group.count() < 1:
        app.group.create(Group("New group name"))
    app.group.delete()
