from model.contact import Contact
from model.user import User


def test_create_user1(app):
    c = Contact(name="Name", middle_name="MiddleName", last_name="LastName", email="email@email.com")
    contact_list_at_start = app.contact.get_list()
    app.contact.create(c)
    assert len(contact_list_at_start) + 1 == app.contact.count()
    contact_list_after_addition = app.contact.get_list()

    expected_contact_list = contact_list_at_start.copy()
    expected_contact_list.append(c)

    assert sorted(expected_contact_list, key=Contact.id_with_none) == sorted(contact_list_after_addition,
                                                                             key=Contact.id_with_none)


def test_create_user2(app):
    c = Contact(name="Name2", middle_name="MiddleName2", last_name="LastName2", email="email2@email.com")
    contact_list_at_start = app.contact.get_list()
    app.contact.create(c)
    assert len(contact_list_at_start) + 1 == app.contact.count()
    contact_list_after_addition = app.contact.get_list()

    expected_contact_list = contact_list_at_start.copy()
    expected_contact_list.append(c)

    assert sorted(expected_contact_list, key=Contact.id_with_none) == sorted(contact_list_after_addition,
                                                                             key=Contact.id_with_none)
