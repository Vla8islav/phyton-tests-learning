from model.group import Group
from selenium.webdriver.support.ui import Select


class ContactGroupRelationHelper:

    def __init__(self, app):
        self.app = app

    def add_contact_to_group(self, contact, group):
        self.app.contact.open_list_page()
        self.app.contact.check_contact_in_a_list_by_id(contact.contact_id)
        self.select_group_on_contact_list_page_by_id(group.id)
        self.app.wd.find_element_by_css_selector("input[name='add']").click()

    def select_group_on_contact_list_page_by_id(self, id):
        group_selector = Select(self.app.wd.find_element_by_name("to_group"))
        group_selector.select_by_value(str(id))

    def press_remove_from_group_button(self):
        self.app.wd.find_element_by_name("remove").click()

    def remove_contact_from_group(self, contact_id, group_id):
        self.app.group.open_specific_group_page(group_id)
        self.app.contact.check_contact_in_a_list_by_id(contact_id)
        self.press_remove_from_group_button()

