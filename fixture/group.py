from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        self.open_creation_page()
        self.fill_info_fields(group)
        self.click_submit_data_button()
        self.go_back_to_group_page()

    def modify_group(self, group, index):
        self.open_groups_page()
        self.click_on_a_checkbox_of_a_group(index)
        self.click_modify_button()
        self.fill_info_fields(group)
        self.click_update_data_button()
        self.go_back_to_group_page()

    def modify_first_group(self):
        self.modify_group(0)

    def delete(self, index):
        self.open_groups_page()
        self.delete_group(index)
        self.go_back_to_group_page()

    def click_update_data_button(self):
        # Update group data
        self.group_cache = None
        self.app.wd.find_element_by_name("update").click()

    def click_submit_data_button(self):
        # Submit group data
        self.group_cache = None
        self.app.wd.find_element_by_name("submit").click()

    def click_modify_button(self):
        self.group_cache = None
        self.app.wd.find_element_by_name("edit").click()

    def click_on_a_delete_group_button(self):
        self.group_cache = None
        self.app.wd.find_element_by_name("delete").click()

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
            self.app.open_page_relative("/group.php")

    def open_specific_group_page(self, group_id):
        relative_group_url = "/?group=%s" % group_id
        if not (self.app.wd.current_url.endswith(relative_group_url)):
            self.app.open_page_relative(relative_group_url)

    def delete_group(self, index):
        self.click_on_a_checkbox_of_a_group(index)
        self.click_on_a_delete_group_button()

    def delete_first_group(self):
        self.delete_group(0)

    def click_on_a_checkbox_of_a_group(self, index):
        self.app.wd.find_elements_by_css_selector("span.group input[type='checkbox']")[index].click()

    def click_on_a_checkbox_of_a_first_group(self):
        self.click_on_a_checkbox_of_a_group(0)

    def go_back_to_group_page(self):
        self.app.wd.find_element_by_link_text("group page").click()

    def count(self):
        self.open_groups_page()
        return len(self.app.wd.find_elements_by_css_selector("input[type='checkbox'][name='selected[]']"))

    group_cache = None

    def get_list(self):
        if self.group_cache is None:
            self.open_groups_page()
            group_web_elements = self.app.wd.find_elements_by_css_selector("span.group")

            self.group_cache = []
            for table_row in group_web_elements:
                input_inside_element = table_row.find_element_by_css_selector("input")
                current_group_id = input_inside_element.get_property("value")
                self.group_cache.append(Group(name=table_row.text, group_id=int(current_group_id)))

        return self.group_cache.copy()
