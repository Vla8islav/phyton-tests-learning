from model.group import Group
from model.user import User


def test_group_create_empty_values(app):
    group = Group("", "", "")
    app.group.create(group)


def test_group_create(app):
    group = Group("Some text 01", "Some text 02", "some text 03")
    app.group.create(group)


