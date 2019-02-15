import pytest
from model.group import Group
from model.user import User
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group_create_empty_values(app):
    group = Group("", "", "")
    app.login(User("admin", "secret"))
    app.create_group(group)
    app.logout()


def test_group_create(app):
    group = Group("Some text 01", "Some text 02", "some text 03")
    app.login(User("admin", "secret"))
    app.create_group(group)
    app.logout()


