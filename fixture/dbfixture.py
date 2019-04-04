import pymysql

from model.group import Group


class DbFixture:
    def __init__(self, host="localhost", database="addressbook", user="root",
                 password=""):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=self.host, database=self.database, user=self.user,
                                          password=self.password, autocommit=True)

    def get_group_list(self):
        retval = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select group_id, group_name, group_header, group_footer from group_list order by group_name, group_id")
            for row in cursor:
                (id, name, header, footer) = row
                retval.append(Group(group_id=id, name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return retval

    def destroy(self):
        self.connection.close()
