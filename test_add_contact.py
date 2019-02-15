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
        c = Contact("Name", "MiddleName", "LastName", "email@email.com")
        self.open_home_page()
        self.login(User("admin", "secret"))
        self.go_to_user_creation_page()
        self.fill_contact_info_fields(c)
        self.submit_form()
        self.logout()

    def test_create_user2(self):
        c = Contact("Name2", "MiddleName2", "LastName2", "email2@email.com")
        self.open_home_page()
        self.login(User("admin", "secret"))
        self.go_to_user_creation_page()
        self.fill_contact_info_fields(c)
        self.submit_form()
        self.logout()

    def submit_form(self):
        self.wd.find_element_by_css_selector(
            "input[value='Enter']").click()
        self.wd.find_element_by_link_text("home").click()

    def fill_contact_info_fields(self, contact):
        self.wd.find_element_by_name("firstname").click()
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.name)
        self.wd.find_element_by_name("middlename").clear()
        self.wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        self.wd.find_element_by_name("lastname").clear()
        self.wd.find_element_by_name("lastname").send_keys(contact.last_name)
        self.wd.find_element_by_name("email").click()
        self.wd.find_element_by_name("email").clear()
        self.wd.find_element_by_name("email").send_keys(contact.email)

    def go_to_user_creation_page(self):
        self.wd.find_element_by_id("footer").click()
        self.wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        # Open home page
        self.wd.get("http://localhost/addressbook/index.php")

    def login(self, user):
        # Login
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(user.username)
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(user.password)
        self.wd.find_element_by_css_selector("input[value='Login']").click()

    def logout(self):
        # Logout
        self.wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

