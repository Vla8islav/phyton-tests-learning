from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() < 1:
        app.contact.create(Contact("New contact name"))
    c = Contact("Name3", "MiddleName3", "LastName3", "email3@email.com")

    contact_list_at_start = app.contact.get_list()
    app.contact.modify_first_contact(c)
    contact_list_after_modification = app.contact.get_list()

    expected_contact_list = contact_list_at_start.copy()
    c.id = contact_list_at_start[0].id
    expected_contact_list[0] = c

    assert sorted(expected_contact_list, key=Contact.id_with_none) == sorted(contact_list_after_modification,
                                                                             key=Contact.id_with_none)

