from random import randint

from model.contact import Contact


def test_delete_contact(app, db, check_ui):
    if app.contact.count() < 1:
        app.contact.create(Contact(name="FirstName", last_name='lastname', middle_name='middleName', email='232322',
                                   email2='12121@243.ru', email3='7777@vfd.re', phone_fax='34234', phone_home='3243242',
                                   phone_mobile='23432', phone_work='321312'))
    contact_list_at_start = db.get_contact_list()
    index = randint(0, len(contact_list_at_start) - 1)
    app.contact.delete_contact(index)
    contact_list_after_deletion = db.get_contact_list()
    assert len(contact_list_at_start) - 1 == len(contact_list_after_deletion)
    expected_contact_list = contact_list_at_start.copy()
    expected_contact_list[index:index+1] = []
    assert contact_list_after_deletion == expected_contact_list
    if check_ui:
        assert sorted(app.contact.get_list(), key=Contact.id_with_none) == \
               sorted(expected_contact_list, key=Contact.id_with_none)
