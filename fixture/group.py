class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        self.open_groups_page()
        self.open_creation_page()
        self.fill_info_fields(group)
        self.submit_data()
        self.go_back_to_group_page()

    def modify_group(self, group):
        self.open_groups_page()
        self.modify_first_group(group)

    def modify_first_group(self, group):
        self.click_on_a_checkbox_of_a_first_group()
        self.click_modify_button()
        self.fill_info_fields(group)
        self.update_data()
        self.go_back_to_group_page()

    def delete(self):
        self.open_groups_page()
        self.delete_first_group()
        self.go_back_to_group_page()

    def update_data(self):
        # Submit group data
        self.app.wd.find_element_by_name("update").click()

    def submit_data(self):
        # Submit group data
        self.app.wd.find_element_by_name("submit").click()

    def click_modify_button(self):
        self.app.wd.find_element_by_name("edit").click()

    def fill_info_fields(self, group):
        # Fill group data
        self.app.wd.find_element_by_name("group_name").click()
        self.app.wd.find_element_by_name("group_name").clear()
        self.app.wd.find_element_by_name("group_name").send_keys(group.name)
        self.app.wd.find_element_by_name("group_header").clear()
        self.app.wd.find_element_by_name("group_header").send_keys(group.header)
        self.app.wd.find_element_by_name("group_footer").clear()
        self.app.wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_creation_page(self):
        # Create a new group
        self.app.wd.find_element_by_name("new").click()

    def open_groups_page(self):
        # Go to groups page
        self.app.wd.get("http://localhost/addressbook/group.php")
#        self.app.wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        self.click_on_a_checkbox_of_a_first_group()
        self.click_on_a_delete_group_button()

    def click_on_a_checkbox_of_a_first_group(self):
        self.app.wd.find_element_by_css_selector("span.group input[type='checkbox']").click()

    def click_on_a_delete_group_button(self):
        self.app.wd.find_element_by_name("delete").click()

    def go_back_to_group_page(self):
        self.app.wd.find_element_by_link_text("group page").click()
