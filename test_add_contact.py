import pytest
from contact import Contact
from user import User
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_user1(app):
    c = Contact("Name", "MiddleName", "LastName", "email@email.com")
    app.login(User("admin", "secret"))
    app.create_contact(c)
    app.logout()


def test_create_user2(app):
    c = Contact("Name2", "MiddleName2", "LastName2", "email2@email.com")
    app.login(User("admin", "secret"))
    app.create_contact(c)
    app.logout()



