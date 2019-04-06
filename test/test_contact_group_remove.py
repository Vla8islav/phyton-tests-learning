from model.contact import Contact
from model.contact_group_relation import ContactGroupRelation
from model.group import Group


def test_contact_to_group_remove(app, db, check_ui):
    contact_group_relations = db.get_contact_group_relations()
    if len(contact_group_relations) == 0:
        app.group.create(Group(name="New group name"))
        app.contact.create(Contact(name="FirstName"))
        app.contact_group_relation.add_contact_to_group(db.get_contacts_without_groups()[0],
                                                        db.get_groups_without_contacts()[0])
        contact_group_relations = db.get_contact_group_relations()

    relation = contact_group_relations[0]
    app.contact_group_relation.remove_contact_from_group(contact_id=relation.contact_id, group_id=relation.group_id)
    contact_group_relations_after_removal = db.get_contact_group_relations()
    assert not ContactGroupRelation(contact_id=relation.contact_id, group_id=relation.group_id) \
               in contact_group_relations_after_removal
