from random import randint

from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() < 1:
        app.contact.create(Contact(name="New contact name"))
    c = Contact(name="Name%s" % randint(0, 10),middle_name= "MiddleName3",last_name= "LastName3",email= "email3@email.com")

    index = randint(0, app.contact.count()-1)
    contact_list_at_start = app.contact.get_list()
    app.contact.modify_contact(c, index)
    assert len(contact_list_at_start) == app.contact.count()
    contact_list_after_modification = app.contact.get_list()

    expected_contact_list = contact_list_at_start.copy()
    c.id = contact_list_at_start[index].id
    expected_contact_list[index] = c

    assert sorted(expected_contact_list, key=Contact.id_with_none) == sorted(contact_list_after_modification,
                                                                             key=Contact.id_with_none)

