from sys import maxsize


class Contact:

    def __init__(self, name=None, middle_name=None, last_name=None, email=None, contact_id=None):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.id = contact_id

    def __repr__(self):
        return "Id\t'%s'\tName\t'%s'\tLast name\t'%s'\tMiddle name\t'%s'\tEmail\t'%s'" % (self.id, self.name, self.last_name, self.middle_name, self.email)

    def __eq__(self, other):
        return self.name == other.name and (self.id is None or other.id is None or self.id == other.id)

    def id_with_none(g):
        if g.id:
            return g.id
        else:
            return maxsize
