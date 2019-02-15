from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()

    def create_group(self, group):
        self.go_to_groups_page()
        self.create_new_group()
        self.fill_group_data(group)
        self.submit_group_data()

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

    def open_home_page(self):
        # Open home page
        self.wd.get("http://localhost/addressbook/index.php")

    def create_contact(self, c):
        self.go_to_user_creation_page()
        self.fill_contact_info_fields(c)
        self.submit_form()

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

