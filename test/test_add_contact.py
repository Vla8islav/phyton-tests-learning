from model.contact import Contact


def test_contact_create(app, json_contacts):
    contact_list_at_start = app.contact.get_list()
    app.contact.create(json_contacts)
    assert len(contact_list_at_start) + 1 == app.contact.count()
    contact_list_after_addition = app.contact.get_list()

    expected_contact_list = contact_list_at_start.copy()
    expected_contact_list.append(json_contacts)

    assert sorted(expected_contact_list, key=Contact.id_with_none) == sorted(contact_list_after_addition,
                                                                             key=Contact.id_with_none)
