from model.group import Group
from model.user import User


def test_group_create_empty_values(app):
    group = Group("New value1", "val2", "val3")
    app.session.login(User("admin", "secret"))
    app.group.modify_group(group)
    app.session.logout()



