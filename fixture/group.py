from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
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
        self.app.ge.type("[name='group_name']", group.name)
        self.app.ge.type("[name='group_header']", group.header)
        self.app.ge.type("[name='group_footer']", group.footer)

    def open_creation_page(self):
        # Create a new group
        self.open_groups_page()
        self.app.wd.find_element_by_name("new").click()

    def open_groups_page(self):
        if not (self.app.wd.current_url.endswith("/group.php") and
                len(self.app.wd.find_elements_by_css_selector("input[value='Delete group(s)'][name='delete']")) > 0):
            self.app.wd.get("http://localhost/addressbook/group.php")

    def delete_first_group(self):
        self.click_on_a_checkbox_of_a_first_group()
        self.click_on_a_delete_group_button()

    def click_on_a_checkbox_of_a_first_group(self):
        self.app.wd.find_element_by_css_selector("span.group input[type='checkbox']").click()

    def click_on_a_delete_group_button(self):
        self.app.wd.find_element_by_name("delete").click()

    def go_back_to_group_page(self):
        self.app.wd.find_element_by_link_text("group page").click()

    def count(self):
        self.open_groups_page()
        return len(self.app.wd.find_elements_by_css_selector("input[type='checkbox'][name='selected[]']"))

    def get_list(self):
        self.open_groups_page()
        group_web_elements = self.app.wd.find_elements_by_css_selector("span.group")

        group_list = []
        for table_row in group_web_elements:
            input_inside_element = table_row.find_element_by_css_selector("input")
            current_group_id = input_inside_element.get_property("value")
            group_list.append(Group(name=table_row.text, group_id=int(current_group_id)))

        return group_list
