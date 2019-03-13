from sys import maxsize


class Contact:

    def __init__(self, name=None, middle_name=None, last_name=None, email=None, email2=None, email3=None,
                 contact_id=None, phone_home=None, phone_mobile=None,
                 phone_work=None, phone_fax=None, address=None,
                 email_list=None, phone_list=None):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.contact_id = contact_id
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.phone_fax = phone_fax
        self.address = address

        self.email_list = email_list
        self.phone_list = phone_list

    def __repr__(self):
        return "Id\t'%s'\tName\t'%s'\tLast name\t'%s'\tMiddle name\t'%s'\tEmail\t'%s'" % (
            self.contact_id, self.name, self.last_name, self.middle_name, self.email)

    def __eq__(self, other):
        return self.name == other.name and self.last_name == other.last_name

    def id_with_none(c):
        if c.contact_id:
            return c.contact_id
        else:
            return maxsize

    def email_list_representation(self):
        retval = self.email_list
        if retval is None:
            retval = self.concatenate_without_null([self.email, self.email2, self.email3])
        return retval

    def phone_list_representation(self):
        retval = self.phone_list
        if retval is None:
            retval = self.concatenate_without_null([self.phone_home, self.phone_mobile, self.phone_work])
        return retval

    @staticmethod
    def concatenate_without_null(array_of_strings):
        return '\n'.join(filter(None, array_of_strings))
