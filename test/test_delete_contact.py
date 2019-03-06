from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() < 1:
        app.contact.create(Contact("New group name"))
    contact_list_at_start = app.contact.get_list()
    app.contact.delete_first_contact()
    assert len(contact_list_at_start) - 1 == app.contact.count()
    contact_list_after_deletion = app.contact.get_list()
    expected_contact_list = contact_list_at_start.copy()
    expected_contact_list[0:1] = []
    assert contact_list_after_deletion == expected_contact_list
