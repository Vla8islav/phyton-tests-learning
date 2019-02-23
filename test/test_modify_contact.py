from model.contact import Contact
from model.user import User


def test_modify_first_contact(app):
    c = Contact("Name3", "MiddleName3", "LastName3", "email3@email.com")
    app.contact.modify_first_contact(c)

