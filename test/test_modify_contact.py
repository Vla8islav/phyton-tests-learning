from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() < 1:
        app.contact.create(Contact("New contact name"))
    c = Contact("Name3", "MiddleName3", "LastName3", "email3@email.com")
    app.contact.modify_first_contact(c)

