from model.group import Group


def test_group_create(app, db, check_ui, json_groups):
    group = json_groups
    group_list_at_start = db.get_group_list()
    app.group.create(group)
    group_list_after_creation = db.get_group_list()
    assert len(group_list_at_start) + 1 == len(group_list_after_creation)
    expected_group_list = group_list_at_start.copy()
    expected_group_list.append(group)

    assert sorted(expected_group_list, key=Group.id_with_none) == sorted(group_list_after_creation,
                                                                         key=Group.id_with_none)
    if check_ui:
        assert sorted(expected_group_list, key=Group.id_with_none) == sorted(app.group.get_list(),
                                                                             key=Group.id_with_none)
