import pymysql

from model.contact import Contact
from model.contact_group_relation import ContactGroupRelation
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
                                     login, role from addressbook where deprecated is null order by lastname, firstname, id")
            for row in cursor:
                (domain_id, id, firstname, middlename, lastname, nickname, company, title, address,
                 addr_long, addr_lat, addr_status, home, mobile, work, fax, email, email2, email3,
                 im, im2, im3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2,
                 notes, photo, x_vcard, x_activesync, created, modified, deprecated, password,
                 login, role) = row
                retval.append(Contact(contact_id=id, name=firstname, last_name=lastname,
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
                "select group_id, group_name, group_header, group_footer from group_list "
                "where deprecated is null order by group_name, group_id")
            for row in cursor:
                (id, name, header, footer) = row
                retval.append(Group(group_id=id, name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return retval

    def destroy(self):
        self.connection.close()

    def get_contacts_without_groups(self):
        retval = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select a.domain_id, a.id, a.firstname, a.middlename, a.lastname, a.nickname, a.company, a.title, a.address,\
                       addr_long, a.addr_lat, a.addr_status, a.home, a.mobile, a.work, a.fax, a.email, a.email2, a.email3,\
                       im, a.im2, a.im3, a.homepage, a.bday, a.bmonth, a.byear, a.aday, a.amonth, a.ayear, a.address2, a.phone2,\
                       notes, a.photo, a.x_vcard, a.x_activesync, a.created, a.modified, a.deprecated, a.password,\
                       login, a.role from addressbook a\
                left join address_in_groups aig on aig.id = a.id\
                    where (aig.id is null)\
                      and a.deprecated is null order by firstname, a.id desc")

            for row in cursor:
                (domain_id, id, firstname, middlename, lastname, nickname, company, title, address,
                 addr_long, addr_lat, addr_status, home, mobile, work, fax, email, email2, email3,
                 im, im2, im3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2,
                 notes, photo, x_vcard, x_activesync, created, modified, deprecated, password,
                 login, role) = row
                retval.append(Contact(contact_id=id, name=firstname, last_name=lastname,
                                      middle_name=middlename, email=email,
                                      email2=email2, email3=email3,
                                      phone_fax=fax, phone_home=home,
                                      phone_mobile=mobile, phone_work=work))
        finally:
            cursor.close()
        return retval

    def get_groups_without_contacts(self):
        retval = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select gl.group_id, gl.group_name, gl.group_header, gl.group_footer from group_list gl \
            left join address_in_groups aig on aig.group_id = gl.group_id \
                    where (aig.id is null)\
                and gl.deprecated is null order by group_name, group_id")
            for row in cursor:
                (id, name, header, footer) = row
                retval.append(Group(group_id=id, name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return retval

    def get_contact_group_relations(self):
        retval = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select distinct aig.group_id, aig.id from address_in_groups aig \
                join addressbook a on aig.id = a.id \
                join group_list gl on aig.group_id = gl.group_id \
                    where aig.deprecated is null and gl.deprecated is null and a.deprecated is null")
            for row in cursor:
                (group_id, contact_id) = row
                retval.append(ContactGroupRelation(contact_id=contact_id, group_id=group_id))
        finally:
            cursor.close()
        return retval

