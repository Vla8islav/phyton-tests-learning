class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, c):
        self.open_creation_page()
        self.fill_info_fields(c)
        self.submit_form()

    def delete_first_contact(self):
        self.open_list_page()
        self.check_first_contact_in_a_list()
        self.click_delete_button()
        self.confirm_contact_deletion()

    def submit_form(self):
        self.app.wd.find_element_by_css_selector(
            "input[value='Enter']").click()
        self.app.wd.find_element_by_link_text("home page").click()

    def fill_info_fields(self, contact):
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

    def open_creation_page(self):
        self.app.wd.find_element_by_id("footer").click()
        self.app.wd.find_element_by_link_text("add new").click()

    def open_list_page(self):
        self.app.wd.find_element_by_xpath("//a[.='home']").click()

    def check_first_contact_in_a_list(self):
        self.get_all_contacts_in_a_list().click()

    def get_all_contacts_in_a_list(self):
        return self.app.wd.find_element_by_css_selector("input[type=checkbox]")

    def click_delete_button(self):
        self.app.wd.find_element_by_css_selector("input[value='Delete']").click()

    def confirm_contact_deletion(self):
        alert = self.app.wd.switch_to_alert()
        alert.accept()
