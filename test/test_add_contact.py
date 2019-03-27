import random
import string

import pytest

from generator.random_string import random_string
from model.contact import Contact
from model.user import User

test_data = [
    Contact(name=random_string("FirstName", 10), last_name=random_string('lastname', 10),
            middle_name=random_string('middleName', 10), email=random_string('232322', 10),
            email2=random_string('12121@243.ru', 10), email3=random_string('7777@vfd.re', 10),
            phone_fax=random_string('34234', 10), phone_home=random_string('3243242', 10),
            phone_mobile=random_string('+7(916) 111-22-33', 10), phone_work=random_string('321312', 10))
    for i in range(5)]


@pytest.mark.parametrize("c", test_data, ids=[repr(x) for x in test_data])
def test_create_user2(app, c):
    contact_list_at_start = app.contact.get_list()
    app.contact.create(c)
    assert len(contact_list_at_start) + 1 == app.contact.count()
    contact_list_after_addition = app.contact.get_list()

    expected_contact_list = contact_list_at_start.copy()
    expected_contact_list.append(c)

    assert sorted(expected_contact_list, key=Contact.id_with_none) == sorted(contact_list_after_addition,
                                                                             key=Contact.id_with_none)
