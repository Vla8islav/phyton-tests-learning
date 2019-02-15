class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        self.open_groups_page()
        self.open_creation_page()
        self.fill_info_fields(group)
        self.submit_data()

    def submit_data(self):
        # Submit group data
        self.app.wd.find_element_by_name("submit").click()

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
        self.app.wd.find_element_by_link_text("groups").click()
