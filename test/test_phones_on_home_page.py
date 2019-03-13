from model.contact import Contact


def test_check_if_contact_info_list_matches_an_actual_info(app):
    if app.contact.count() < 1:
        app.contact.create(Contact(name="FirstName", last_name='lastname', middle_name='middleName', email='232322',
                                   email2='12121@243.ru', email3='7777@vfd.re', phone_fax='34234', phone_home='3243242',
                                   phone_mobile='23432', phone_work='321312'))
    contact_list_index = 0
    contact_info_from_contact_list = app.contact.get_list()[contact_list_index]
    contact_info_from_contact_page = app.contact.get_contact_info_from_edit_page(
        contact_info_from_contact_list.contact_id)
    assert (contact_info_from_contact_page.name == contact_info_from_contact_list.name)
    #    assert (contact_info_from_contact_page.middle_name == contact_info_from_contact_list.middle_name)
    assert (contact_info_from_contact_page.last_name == contact_info_from_contact_list.last_name)
    assert (contact_info_from_contact_page.email_list_representation() ==
            contact_info_from_contact_list.email_list_representation())
    #    assert (contact_info_from_contact_page.email == contact_info_from_contact_list.email)
    #    assert (contact_info_from_contact_page.email2 == contact_info_from_contact_list.email2)
    #    assert (contact_info_from_contact_page.email3 == contact_info_from_contact_list.email3)
    assert (contact_info_from_contact_page.contact_id == contact_info_from_contact_list.contact_id)
    assert (contact_info_from_contact_page.phone_list_representation() ==
            contact_info_from_contact_list.phone_list_representation())
    #    assert (contact_info_from_contact_page.phone_home == contact_info_from_contact_list.phone_home)
    #    assert (contact_info_from_contact_page.phone_mobile == contact_info_from_contact_list.phone_mobile)
    #    assert (contact_info_from_contact_page.phone_work == contact_info_from_contact_list.phone_work)
    #    assert (contact_info_from_contact_page.phone_fax == contact_info_from_contact_list.phone_fax)
    assert (contact_info_from_contact_page.address == contact_info_from_contact_list.address)
