# -*- coding: utf-8 -*-
from selenium import webdriver
from user import User
from contact import Contact
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_user1_create(self):
        wd = self.wd
        self.OpenHomePage(wd)
        self.Login(wd, User("admin", "secret"))
        self.GoToUserCreationPage(wd)
        c = Contact("Name", "MiddleName", "LastName", "email@email.com")
        self.FillUserInfoFields(c, wd)
        self.SubmitForm(wd)
        self.Logout(wd)

    def test_user2_create(self):
        wd = self.wd
        self.OpenHomePage(wd)
        self.Login(wd, User("admin", "secret"))
        self.GoToUserCreationPage(wd)
        c = Contact("Name2", "MiddleName2", "LastName2", "email2@email.com")
        self.FillUserInfoFields(c, wd)
        self.SubmitForm(wd)
        self.Logout(wd)

    def SubmitForm(self, wd):
        wd.find_element_by_css_selector(
            "input[value='Enter']").click()
        wd.find_element_by_link_text("home").click()

    def FillUserInfoFields(self, c, wd):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(c.Name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(c.MiddleName)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(c.LastName)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(c.Email)

    def GoToUserCreationPage(self, wd):
        wd.find_element_by_id("footer").click()
        wd.find_element_by_link_text("add new").click()

    def OpenHomePage(self, wd):
        # Open home page
        wd.get("http://localhost/addressbook/index.php")

    def Login(self, wd, user):
        # Login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user.username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user.password)
        wd.find_element_by_css_selector("input[value='Login']").click()

    def Logout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

