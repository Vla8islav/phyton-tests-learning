from model.group import Group
from model.user import User


def test_group_modify_first_group(app):
    group = Group("New value1", "val2", "val3")
    app.session.login(User("admin", "secret"))
    app.group.modify_group(group)
    app.session.logout()


def test_group_modify_first_group_name_only(app):
    group = Group("New value1_name_only")
    app.session.login(User("admin", "secret"))
    app.group.modify_group(group)
    app.session.logout()

