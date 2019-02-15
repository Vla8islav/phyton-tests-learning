# -*- coding: utf-8 -*-
from user import User
from contact import Contact
import unittest
from application import Application


class AddContactTestCase(unittest.TestCase):
    def setUp(self):
        self.App = Application()

    def tearDown(self):
        self.App.destroy()

    def test_create_user1(self):
        c = Contact("Name", "MiddleName", "LastName", "email@email.com")
        self.App.login(User("admin", "secret"))
        self.App.create_contact(c)
        self.App.logout()

    def test_create_user2(self):
        c = Contact("Name2", "MiddleName2", "LastName2", "email2@email.com")
        self.App.login(User("admin", "secret"))
        self.App.create_contact(c)
        self.App.logout()


if __name__ == "__main__":
    unittest.main()

