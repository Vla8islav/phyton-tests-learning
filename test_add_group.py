from selenium import webdriver
from group import Group
from user import User
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_empty_group(self):
        wd = self.wd
        self.OpenHomePage(wd)
        self.Login(wd, User("admin", "secret"))
        self.CreateGroup(wd, Group("", "", ""))
        self.Logout(wd)

    def test_add_group(self):
        wd = self.wd
        self.OpenHomePage(wd)
        self.Login(wd, User("admin", "secret"))
        self.CreateGroup(wd, Group("Some text 01", "Some text 02", "some text 03"))
        self.Logout(wd)

    def CreateGroup(self, wd, group):
        self.GoToGroupPage(wd)
        self.GoToGroupCreationPage(wd)
        self.FillGroupData(wd, group)
        self.SubmitGroupData(wd)

    def Logout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def SubmitGroupData(self, wd):
        # Submit group data
        wd.find_element_by_name("submit").click()

    def FillGroupData(self, wd, group):
        # Fill group data
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def GoToGroupCreationPage(self, wd):
        # Create a new group
        wd.find_element_by_name("new").click()

    def GoToGroupPage(self, wd):
        # Go to groups page
        wd.find_element_by_link_text("groups").click()

    def Login(self, wd, user):
        # Login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user.username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user.password)
        wd.find_element_by_css_selector("input[value='Login']").click()

    def OpenHomePage(self, wd):
        # Open home page
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
