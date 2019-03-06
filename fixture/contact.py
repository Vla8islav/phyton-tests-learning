from model.contact import Contact


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
        self.list_cache = None
        self.app.wd.find_element_by_link_text("home page").click()

    def update_contact(self):
        self.app.wd.find_element_by_css_selector(
            "input[value='Update']").click()
        self.list_cache = None
        self.app.wd.find_element_by_link_text("home page").click()

    def fill_info_fields(self, contact):
        # Fill group data
        self.app.ge.type("[name='firstname']", contact.name)
        self.app.ge.type("[name='middlename']", contact.middle_name)
        self.app.ge.type("[name='lastname']", contact.last_name)
        self.app.ge.type("[name='email']", contact.email)

    def open_creation_page(self):
        if not (self.app.wd.current_url.endswith("/edit.php") and
                len(self.app.wd.find_elements_by_css_selector("input[name=submit][value=Enter]")) > 0):
            self.app.wd.find_element_by_id("footer").click()
            self.app.wd.find_element_by_link_text("add new").click()

    def open_list_page(self):
        if not ((self.app.wd.current_url.endswith("/") and
                 len(self.app.wd.find_elements_by_css_selector("input[type=button][value='Send e-Mail']")) > 0)) \
                or not self.app.wd.current_url.endswith("/"):
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
        self.list_cache = None

    def count(self):
        self.open_list_page()
        return len(self.app.wd.find_elements_by_css_selector("input[type='checkbox'][name='selected[]']"))

    list_cache = None

    def get_list(self):
        if self.list_cache is None:
            self.open_list_page()
            self.app.wd.refresh()
            contact_web_elements = self.app.wd.find_elements_by_css_selector("table tbody tr[name=entry]")

            self.list_cache = []
            if contact_web_elements is not None:
                for contact_row in contact_web_elements:
                    contact_columns = contact_row.find_elements_by_css_selector("td")
                    contact_id = contact_columns[0].find_element_by_css_selector("input").get_property("value")
                    last_name = contact_columns[1].text
                    first_name = contact_columns[2].text
                    address = contact_columns[3].text
                    email = contact_columns[4].text
                    phone_list = contact_columns[5].text

                    self.list_cache.append(
                        Contact(contact_id=int(contact_id), name=first_name, last_name=last_name, email=email))

        return self.list_cache.copy()
