from model.user import User


def test_delete_first_group(app):
    app.session.login(User("admin", "secret"))
    app.group.delete()
    app.session.logout()


