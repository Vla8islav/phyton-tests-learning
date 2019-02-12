# -*- coding: utf-8 -*-
from selenium import webdriver
from user import User
from contact import Contact
import unittest


class AddContactTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_create_user1(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User("admin", "secret"))
        self.go_to_user_creation_page(wd)
        c = Contact("Name", "MiddleName", "LastName", "email@email.com")
        self.fill_user_info_fields(c, wd)
        self.submit_form(wd)
        self.logout(wd)

    def test_create_user2(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User("admin", "secret"))
        self.go_to_user_creation_page(wd)
        c = Contact("Name2", "MiddleName2", "LastName2", "email2@email.com")
        self.fill_user_info_fields(c, wd)
        self.submit_form(wd)
        self.logout(wd)

    def submit_form(self, wd):
        wd.find_element_by_css_selector(
            "input[value='Enter']").click()
        wd.find_element_by_link_text("home").click()

    def fill_user_info_fields(self, c, wd):
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

    def go_to_user_creation_page(self, wd):
        wd.find_element_by_id("footer").click()
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self, wd):
        # Open home page
        wd.get("http://localhost/addressbook/index.php")

    def login(self, wd, user):
        # Login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user.username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user.password)
        wd.find_element_by_css_selector("input[value='Login']").click()

    def logout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

