import random
import string

import pytest

from generator.random_string import random_string
from model.group import Group


def test_group_modify_group(app, json_groups, db, check_ui):
    if len(db.get_group_list()) < 1:
        app.group.create(Group(random_string("New group name", 10)))
    index = random.randint(0, len(db.get_group_list()) - 1)
    group_list_at_start = db.get_group_list()
    app.group.modify_group(json_groups, index)
    group_list_after_modification = db.get_group_list()
    assert len(group_list_at_start) == len(db.get_group_list())
    json_groups.id = group_list_at_start[index].id
    expected_group_list = group_list_at_start.copy()
    expected_group_list[index:index + 1] = [json_groups]
    assert sorted(expected_group_list, key=Group.id_with_none) == sorted(group_list_after_modification,
                                                                             key=Group.id_with_none)
    if check_ui:
        assert sorted(expected_group_list, key=Group.id_with_none) == sorted(app.group.get_list(),
                                                                             key=Group.id_with_none)

