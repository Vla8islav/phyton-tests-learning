import pytest
from model.contact import Contact
from model.user import User
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_user1(app):
    c = Contact("Name", "MiddleName", "LastName", "email@email.com")
    app.session.login(User("admin", "secret"))
    app.contact.create(c)
    app.session.logout()


def test_create_user2(app):
    c = Contact("Name2", "MiddleName2", "LastName2", "email2@email.com")
    app.session.login(User("admin", "secret"))
    app.contact.create(c)
    app.session.logout()
