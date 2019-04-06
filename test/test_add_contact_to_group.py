from model.contact_group_relation import ContactGroupRelation


def test_add_contact_to_group(app, db, check_ui):
    contact = db.get_contacts_without_groups()[0]
    group = db.get_groups_without_contacts()[0]
    app.contact_group_relation.add_contact_to_group(contact, group)
    contact_group_relations = db.get_contact_group_relations()
    assert ContactGroupRelation(contact_id=contact.contact_id, group_id=group.id) in contact_group_relations
