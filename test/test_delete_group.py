from model.group import Group


def test_delete_first_group(app):
    for i in range(0, 100):
        if app.group.count() < 1:
            app.group.create(Group("New group name"))
        app.group.delete()
