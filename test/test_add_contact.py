from model.contact import Contact


def test_contact_create(app, json_contacts, db, check_ui):
    contact_list_at_start = db.get_contact_list()
    app.contact.create(json_contacts)
    assert len(contact_list_at_start) + 1 == len(db.get_contact_list())
    contact_list_after_addition = db.get_contact_list()

    expected_contact_list = contact_list_at_start.copy()
    expected_contact_list.append(json_contacts)

    assert sorted(expected_contact_list, key=Contact.id_with_none) == sorted(contact_list_after_addition,
                                                                             key=Contact.id_with_none)
    if check_ui:
        assert sorted(app.contact.get_list(), key=Contact.id_with_none) == \
               sorted(expected_contact_list, key=Contact.id_with_none)
