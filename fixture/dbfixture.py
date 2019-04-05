import pymysql

from model.contact import Contact
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

    def get_contact_list(self):
        retval = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select domain_id, id, firstname, middlename, lastname, nickname, company, title, address,\
                                     addr_long, addr_lat, addr_status, home, mobile, work, fax, email, email2, email3,\
                                     im, im2, im3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2,\
                                     notes, photo, x_vcard, x_activesync, created, modified, deprecated, password,\
                                     login, role from addressbook")
            for row in cursor:
                (domain_id, id, firstname, middlename, lastname, nickname, company, title, address,
                 addr_long, addr_lat, addr_status, home, mobile, work, fax, email, email2, email3,
                 im, im2, im3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2,
                 notes, photo, x_vcard, x_activesync, created, modified, deprecated, password,
                 login, role) = row
                retval.append(Contact(name=firstname, last_name=lastname,
                                      middle_name=middlename, email=email,
                                      email2=email2, email3=email3,
                                      phone_fax=fax, phone_home=home,
                                      phone_mobile=mobile, phone_work=work))
        finally:
            cursor.close()
        return retval

    def destroy(self):
        self.connection.close()

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
