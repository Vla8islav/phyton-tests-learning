import random
import string

import pytest

from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' ' * 5
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(5)]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_group_create_empty_values(app, group):
    group_list_at_start = app.group.get_list()
    app.group.create(group)
    group_list_after_creation = app.group.get_list()
    assert len(group_list_at_start) + 1 == app.group.count()
    expected_group_list = group_list_at_start.copy()
    expected_group_list.append(group)

    assert sorted(expected_group_list, key=Group.id_with_none) == sorted(group_list_after_creation,
                                                                         key=Group.id_with_none)

