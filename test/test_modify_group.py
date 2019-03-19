import random
import string

import pytest

from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' ' * 5
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(5)]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_group_modify_first_group(app, group):
    if app.group.count() < 1:
        app.group.create(Group(random_string("New group name", 10)))
    group_list_at_start = app.group.get_list()
    index = random.randint(0, app.group.count() - 1)
    app.group.modify_group(group, index)
    group_list_after_modification = app.group.get_list()
    assert len(group_list_at_start) == app.group.count()
    group.id = group_list_at_start[index].id
    expected_new_group_list = group_list_at_start.copy()
    expected_new_group_list[index:index + 1] = [group]
    assert sorted(expected_new_group_list, key=Group.id_with_none) == sorted(group_list_after_modification,
                                                                             key=Group.id_with_none)
