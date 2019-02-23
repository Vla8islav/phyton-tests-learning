from model.contact import Contact
from model.user import User


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
