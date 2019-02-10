from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.OpenHomePage(wd)
        self.Login(wd)
        self.GoToGroupsPage(wd)
        self.CreateNewGroup(wd)
        self.FillGroupData(wd)
        self.SubmitGroupData(wd)
        self.Logout(wd)

    def Logout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def SubmitGroupData(self, wd):
        # Submit group data
        wd.find_element_by_name("submit").click()

    def FillGroupData(self, wd):
        # Fill group data
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Some text 01")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("Some text 02")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("some text 03")

    def CreateNewGroup(self, wd):
        # Create a new group
        wd.find_element_by_name("new").click()

    def GoToGroupsPage(self, wd):
        # Go to groups page
        wd.find_element_by_link_text("groups").click()

    def Login(self, wd):
        # Login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_css_selector("input[value='Login']").click()

    def OpenHomePage(self, wd):
        # Open home page
        wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
