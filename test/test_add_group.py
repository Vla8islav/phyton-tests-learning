from model.group import Group


def test_group_create(app, json_groups):
    group = json_groups
    group_list_at_start = app.group.get_list()
    app.group.create(group)
    group_list_after_creation = app.group.get_list()
    assert len(group_list_at_start) + 1 == app.group.count()
    expected_group_list = group_list_at_start.copy()
    expected_group_list.append(group)

    assert sorted(expected_group_list, key=Group.id_with_none) == sorted(group_list_after_creation,
                                                                         key=Group.id_with_none)

