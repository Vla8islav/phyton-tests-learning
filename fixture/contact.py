from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, c):
        self.open_creation_page()
        self.fill_info_fields(c)
        self.submit_new_contact()

    def modify_contact(self, c, index):
        self.open_list_page()
        self.click_edit_button(index)
        self.fill_info_fields(c)
        self.update_contact()

    def modify_first_contact(self, c):
        self.modify_contact(c, 0)

    def delete_contact(self, index):
        self.open_list_page()
        self.check_contact_in_a_list(index)
        self.click_delete_button()
        self.confirm_contact_deletion()

    def delete_first_contact(self):
        self.delete_contact(0)

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
        self.app.ge.type("[name='home']", contact.phone_home)
        self.app.ge.type("[name='mobile']", contact.phone_mobile)
        self.app.ge.type("[name='work']", contact.phone_work)
        self.app.ge.type("[name='fax']", contact.phone_fax)
        self.app.ge.type("[name='email']", contact.email)
        self.app.ge.type("[name='email2']", contact.email2)
        self.app.ge.type("[name='email3']", contact.email3)

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

    def check_contact_in_a_list(self, index):
        self.app.wd.find_elements_by_css_selector("input[type=checkbox]")[index].click()

    def check_first_contact_in_a_list(self):
        self.check_contact_in_a_list(0)

    def click_edit_button(self, index):
        self.app.wd.find_elements_by_css_selector("td img[title='Edit']")[index].click()

    def click_delete_button(self):
        self.app.wd.find_element_by_css_selector("input[value='Delete']").click()

    def confirm_contact_deletion(self):
        alert = self.app.wd.switch_to_alert()
        alert.accept()
        self.list_cache = None

    def count(self):
        self.open_list_page()
        self.app.wd.refresh()
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
                    email_list = contact_columns[4].text
                    email = email_list
                    phone_list = contact_columns[5].text
                    phone_fax = phone_list

                    self.list_cache.append(
                        Contact(contact_id=int(contact_id), name=first_name, last_name=last_name, email_list=email_list,
                                phone_list=phone_list, address=address))

        return self.list_cache.copy()

    def get_full_contact_info_sting_by_position_in_contact_list(self, contact_list_index):
        contact = self.get_list()[contact_list_index]
        self.open_contact_edit_page_by_id(contact.id)

        contact_full_text_element = self.app.wd.find_element_by_css_selector("div#content")
        return contact_full_text_element.text

    def open_contact_view_page_by_id(self, contact_id):
        self.app.open_page_relative("/addressbook/view.php?id=%s" % contact_id)

    def open_contact_edit_page_by_id(self, contact_id):
        self.app.open_page_relative("/addressbook/edit.php?id=%s" % contact_id)

    def get_contact_info_from_edit_page(self, contact_id):
        self.open_contact_edit_page_by_id(contact_id)
        wd = self.app.wd
        contact = Contact(name=wd.find_element_by_css_selector("[name='firstname']").get_attribute("value"),
                          middle_name=wd.find_element_by_css_selector("[name='middlename']").get_attribute("value"),
                          last_name=wd.find_element_by_css_selector("[name='lastname']").get_attribute("value"),
                          phone_home=wd.find_element_by_css_selector("[name='home']").get_attribute("value"),
                          phone_mobile=wd.find_element_by_css_selector("[name='mobile']").get_attribute("value"),
                          phone_work=wd.find_element_by_css_selector("[name='work']").get_attribute("value"),
                          phone_fax=wd.find_element_by_css_selector("[name='fax']").get_attribute("value"),
                          email=wd.find_element_by_css_selector("[name='email']").get_attribute("value"),
                          email2=wd.find_element_by_css_selector("[name='email2']").get_attribute("value"),
                          email3=wd.find_element_by_css_selector("[name='email3']").get_attribute("value"),
                          address=wd.find_element_by_css_selector("[name='address']").get_attribute("value"),
                          contact_id=contact_id)
        return contact

    def check_that_all_the_data_from_contact_is_present_on_contact_view_page(self, contact_id):
        self.open_contact_view_page_by_id(contact_id)
        wd = self.app.wd
        contact = Contact(name=wd.find_element_by_css_selector("[name='firstname']").get_attribute("value"),
                          middle_name=wd.find_element_by_css_selector("[name='middlename']").get_attribute("value"),
                          last_name=wd.find_element_by_css_selector("[name='lastname']").get_attribute("value"),
                          phone_home=wd.find_element_by_css_selector("[name='home']").get_attribute("value"),
                          phone_mobile=wd.find_element_by_css_selector("[name='mobile']").get_attribute("value"),
                          phone_work=wd.find_element_by_css_selector("[name='work']").get_attribute("value"),
                          phone_fax=wd.find_element_by_css_selector("[name='fax']").get_attribute("value"),
                          email=wd.find_element_by_css_selector("[name='email']").get_attribute("value"),
                          email2=wd.find_element_by_css_selector("[name='email2']").get_attribute("value"),
                          email3=wd.find_element_by_css_selector("[name='email3']").get_attribute("value"),
                          address=wd.find_element_by_css_selector("[name='address']").get_attribute("value"),
                          contact_id=contact_id)
        return contact
