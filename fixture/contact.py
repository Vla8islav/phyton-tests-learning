class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, c):
        self.go_to_user_creation_page()
        self.fill_contact_info_fields(c)
        self.submit_form()

    def submit_form(self):
        self.app.wd.find_element_by_css_selector(
            "input[value='Enter']").click()
        self.app.wd.find_element_by_link_text("home").click()

    def fill_contact_info_fields(self, contact):
        self.app.wd.find_element_by_name("firstname").click()
        self.app.wd.find_element_by_name("firstname").clear()
        self.app.wd.find_element_by_name("firstname").send_keys(contact.name)
        self.app.wd.find_element_by_name("middlename").clear()
        self.app.wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        self.app.wd.find_element_by_name("lastname").clear()
        self.app.wd.find_element_by_name("lastname").send_keys(contact.last_name)
        self.app.wd.find_element_by_name("email").click()
        self.app.wd.find_element_by_name("email").clear()
        self.app.wd.find_element_by_name("email").send_keys(contact.email)

    def go_to_user_creation_page(self):
        self.app.wd.find_element_by_id("footer").click()
        self.app.wd.find_element_by_link_text("add new").click()
