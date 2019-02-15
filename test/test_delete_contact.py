import pytest
from model.contact import Contact
from model.user import User
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_delete_first_contact(app):
    app.session.login(User("admin", "secret"))
    app.contact.delete_first_contact()
    app.session.logout()


