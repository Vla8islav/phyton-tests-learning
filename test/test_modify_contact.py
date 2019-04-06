from random import randint

from model.contact import Contact


def test_modify_first_contact(app, json_contact, db, check_ui):
    if app.contact.count() < 1:
        app.contact.create(Contact(name="New contact name"))
    c = json_contact

    contact_list_at_start = db.get_contact_list()
    index = randint(0, len(contact_list_at_start)-1)
    app.contact.modify_contact(c, index)
    contact_list_after_modification = db.get_contact_list()
    assert len(contact_list_at_start) == len(contact_list_after_modification)

    expected_contact_list = contact_list_at_start.copy()
    c.contact_id = contact_list_at_start[index].contact_id
    expected_contact_list[index] = c

    assert sorted(expected_contact_list, key=Contact.id_with_none) == sorted(contact_list_after_modification,
                                                                             key=Contact.id_with_none)
    if check_ui:
        assert sorted(app.contact.get_list(), key=Contact.id_with_none) == \
               sorted(expected_contact_list, key=Contact.id_with_none)

