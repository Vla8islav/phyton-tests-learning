from model.contact import Contact
from model.user import User


def test_create_user1(app):
    c = Contact("Name", "MiddleName", "LastName", "email@email.com")
    contact_list_at_start = app.contact.get_list()
    app.contact.create(c)
    contact_list_after_addition = app.contact.get_list()

    expected_contact_list = contact_list_at_start.copy()
    expected_contact_list.append(c)

    assert sorted(expected_contact_list, key=Contact.id_with_none) == sorted(contact_list_after_addition,
                                                                             key=Contact.id_with_none)


def test_create_user2(app):
    c = Contact("Name2", "MiddleName2", "LastName2", "email2@email.com")
    contact_list_at_start = app.contact.get_list()
    app.contact.create(c)
    contact_list_after_addition = app.contact.get_list()

    expected_contact_list = contact_list_at_start.copy()
    expected_contact_list.append(c)

    assert sorted(expected_contact_list, key=Contact.id_with_none) == sorted(contact_list_after_addition,
                                                                             key=Contact.id_with_none)
