from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_list()

    def clean(group):
        return Group(group_id=group.id, name=group.name.strip(), header=group.header, )

    db_list = map(clean, db.get_group_list())

    assert sorted(ui_list, key=Group.id_with_none) == sorted(db_list, key=Group.id_with_none)
