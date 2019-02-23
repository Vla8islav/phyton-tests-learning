from model.user import User


def test_delete_first_group(app):
    app.group.delete()


