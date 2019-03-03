from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, group_id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = group_id

    def __repr__(self):
        return "Id\t%s\tName\t%s\t" % (self.id, self.name)

    def __eq__(self, other):
        return self.name == other.name and (self.id is None or other.id is None or self.id == other.id)

    def id_with_none(g):
        if g.id:
            return g.id
        else:
            return maxsize

