from model.user import User


def test_delete_first_contact(app):
    app.session.login(User("admin", "secret"))
    app.contact.delete_first_contact()
    app.session.logout()


