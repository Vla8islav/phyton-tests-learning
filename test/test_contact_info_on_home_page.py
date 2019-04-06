from random import randint

from model.contact import Contact


def test_contact_info_list_matches_database_info(app, db):
    if app.contact.count() < 1:
        app.contact.create(Contact(name="FirstName", last_name='lastname', middle_name='middleName', email='232322',
                                   email2='12121@243.ru', email3='7777@vfd.re', phone_fax='34234', phone_home='3243242',
                                   phone_mobile='8(916) 222-33-44', phone_work='321312'))
    contact_info_list_from_db = db.get_contact_list()
    contact_info_list_ui = app.contact.get_list()

    assert len(contact_info_list_from_db) == len(contact_info_list_ui)

    contact_info_list_from_db = sorted(contact_info_list_from_db, key=Contact.id_with_none)
    contact_info_list_ui = sorted(contact_info_list_ui, key=Contact.id_with_none)
    for i in range(0, len(contact_info_list_from_db)):
        contact_info_db = contact_info_list_from_db[i]
        contact_info_ui = contact_info_list_ui[i]
        assert (contact_info_db.name == contact_info_ui.name)
        assert (contact_info_db.last_name == contact_info_ui.last_name)
        assert (contact_info_db.email_list_representation() ==
                contact_info_ui.email_list_representation())
        assert (contact_info_db.contact_id == contact_info_ui.contact_id)
        assert (contact_info_db.phone_list_representation() ==
                contact_info_ui.phone_list_representation())
        assert (contact_info_db.address_string_representation() == contact_info_ui.address_string_representation())

