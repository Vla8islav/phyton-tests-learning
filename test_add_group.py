from selenium import webdriver
from group import Group
from user import User
from application import Application
import unittest


class AddGroupTestCase(unittest.TestCase):
    def setUp(self):
        self.App = Application()

    def tearDown(self):
        self.App.destroy()

    def test_group_create_empty_values(self):
        group = Group("", "", "")
        self.App.login(User("admin", "secret"))
        self.App.create_group(group)
        self.App.logout()

    def test_group_create(self):
        group = Group("Some text 01", "Some text 02", "some text 03")
        self.App.login(User("admin", "secret"))
        self.App.create_group(group)
        self.App.logout()


if __name__ == "__main__":
    unittest.main()
