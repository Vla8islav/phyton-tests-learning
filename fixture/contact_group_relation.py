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
        # self.app.wd.refresh()

    def select_group_on_contact_list_page_by_id(self, id):
        group_selector = Select(self.app.wd.find_element_by_name("to_group"))
        group_selector.select_by_value(str(id))


