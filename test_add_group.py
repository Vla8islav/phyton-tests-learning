from selenium import webdriver
from group import Group
from user import User
import unittest


class AddGroupTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_group_create_empty_values(self):
        group = Group("", "", "")
        self.open_home_page()
        self.login(User("admin", "secret"))
        self.create_group(group)
        self.logout()

    def test_group_create(self):
        group = Group("Some text 01", "Some text 02", "some text 03")
        self.open_home_page()
        self.login(User("admin", "secret"))
        self.create_group(group)
        self.logout()

    def create_group(self, group):
        self.go_to_groups_page()
        self.create_new_group()
        self.fill_group_data(group)
        self.submit_group_data()

    def logout(self):
        # Logout
        self.wd.find_element_by_link_text("Logout").click()

    def submit_group_data(self):
        # Submit group data
        self.wd.find_element_by_name("submit").click()

    def fill_group_data(self, group):
        # Fill group data
        self.wd.find_element_by_name("group_name").click()
        self.wd.find_element_by_name("group_name").clear()
        self.wd.find_element_by_name("group_name").send_keys(group.name)
        self.wd.find_element_by_name("group_header").clear()
        self.wd.find_element_by_name("group_header").send_keys(group.header)
        self.wd.find_element_by_name("group_footer").clear()
        self.wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create_new_group(self):
        # Create a new group
        self.wd.find_element_by_name("new").click()

    def go_to_groups_page(self):
        # Go to groups page
        self.wd.find_element_by_link_text("groups").click()

    def login(self, user):
        # Login
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(user.username)
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(user.password)
        self.wd.find_element_by_css_selector("input[value='Login']").click()

    def open_home_page(self):
        # Open home page
        self.wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
