from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() < 1:
        app.group.create(Contact("New group name"))
    app.contact.delete_first_contact()
