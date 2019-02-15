import pytest

from fixture.application import Application
from model.user import User


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_delete_first_group(app):
    app.session.login(User("admin", "secret"))
    app.group.delete()
    app.session.logout()


