import random
import string

import pytest

from generator.random_string import random_string
from model.group import Group


def test_group_modify_first_group(app, json_groups):
    if app.group.count() < 1:
        app.group.create(Group(random_string("New group name", 10)))
    group_list_at_start = app.group.get_list()
    index = random.randint(0, app.group.count() - 1)
    app.group.modify_group(json_groups, index)
    group_list_after_modification = app.group.get_list()
    assert len(group_list_at_start) == app.group.count()
    json_groups.id = group_list_at_start[index].id
    expected_new_group_list = group_list_at_start.copy()
    expected_new_group_list[index:index + 1] = [json_groups]
    assert sorted(expected_new_group_list, key=Group.id_with_none) == sorted(group_list_after_modification,
                                                                             key=Group.id_with_none)
