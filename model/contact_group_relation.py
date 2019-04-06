import re
from sys import maxsize


class ContactGroupRelation:

    def __init__(self, contact_id, group_id):
        self.contact_id = contact_id
        self.group_id = group_id

    def __eq__(self, other):
        return self.contact_id == other.contact_id and self.group_id == other.group_id


