class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, c):
        self.open_creation_page()
        self.fill_info_fields(c)
        self.submit_new_contact()

    def modify_first_contact(self, c):
        self.open_list_page()
        self.modify_first_contact_in_a_list()
        self.fill_info_fields(c)
        self.update_contact()

    def delete_first_contact(self):
        self.open_list_page()
        self.check_first_contact_in_a_list()
        self.click_delete_button()
        self.confirm_contact_deletion()

    def submit_new_contact(self):
        self.app.wd.find_element_by_css_selector(
            "input[value='Enter']").click()
        self.app.wd.find_element_by_link_text("home page").click()

    def update_contact(self):
        self.app.wd.find_element_by_css_selector(
            "input[value='Update']").click()
        self.app.wd.find_element_by_link_text("home page").click()

    def fill_info_fields(self, contact):
        # Fill group data
        self.app.ge.type("[name='firstname']", contact.name)
        self.app.ge.type("[name='middlename']", contact.middle_name)
        self.app.ge.type("[name='lastname']", contact.last_name)
        self.app.ge.type("[name='email']", contact.email)

    def open_creation_page(self):
        self.app.wd.find_element_by_id("footer").click()
        self.app.wd.find_element_by_link_text("add new").click()

    def open_list_page(self):
        self.app.wd.find_element_by_xpath("//a[.='home']").click()

    def check_first_contact_in_a_list(self):
        self.app.wd.find_element_by_css_selector("input[type=checkbox]").click()

    def modify_first_contact_in_a_list(self):
        self.app.wd.find_element_by_css_selector("td img[title='Edit']").click()

    def click_delete_button(self):
        self.app.wd.find_element_by_css_selector("input[value='Delete']").click()

    def confirm_contact_deletion(self):
        alert = self.app.wd.switch_to_alert()
        alert.accept()

    def count(self):
        self.open_list_page()
        return len(self.app.wd.find_elements_by_css_selector("input[type='checkbox'][name='selected[]']"))
