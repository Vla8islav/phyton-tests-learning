from selenium import webdriver
from group import Group
from user import User
import unittest


class AddGroupTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_group_create_empty_values(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User("admin", "secret"))
        self.create_group(wd, Group("", "", ""))
        self.logout(wd)

    def test_group_create(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User("admin", "secret"))
        self.create_group(wd, Group("Some text 01", "Some text 02", "some text 03"))
        self.logout(wd)

    def create_group(self, wd, group):
        self.go_to_groups_page(wd)
        self.create_new_group(wd)
        self.fill_group_data(wd, group)
        self.submit_group_data(wd)

    def logout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def submit_group_data(self, wd):
        # Submit group data
        wd.find_element_by_name("submit").click()

    def fill_group_data(self, wd, group):
        # Fill group data
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create_new_group(self, wd):
        # Create a new group
        wd.find_element_by_name("new").click()

    def go_to_groups_page(self, wd):
        # Go to groups page
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, user):
        # Login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user.username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user.password)
        wd.find_element_by_css_selector("input[value='Login']").click()

    def open_home_page(self, wd):
        # Open home page
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
