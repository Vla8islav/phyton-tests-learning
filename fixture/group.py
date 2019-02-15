class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        self.go_to_groups_page()
        self.create_new_group()
        self.fill_group_data(group)
        self.submit_group_data()

    def submit_group_data(self):
        # Submit group data
        self.app.wd.find_element_by_name("submit").click()

    def fill_group_data(self, group):
        # Fill group data
        self.app.wd.find_element_by_name("group_name").click()
        self.app.wd.find_element_by_name("group_name").clear()
        self.app.wd.find_element_by_name("group_name").send_keys(group.name)
        self.app.wd.find_element_by_name("group_header").clear()
        self.app.wd.find_element_by_name("group_header").send_keys(group.header)
        self.app.wd.find_element_by_name("group_footer").clear()
        self.app.wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create_new_group(self):
        # Create a new group
        self.app.wd.find_element_by_name("new").click()

    def go_to_groups_page(self):
        # Go to groups page
        self.app.wd.find_element_by_link_text("groups").click()
