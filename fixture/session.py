class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, user):
        # Login
        self.app.open_home_page()
        self.app.wd.find_element_by_name("user").clear()
        self.app.wd.find_element_by_name("user").send_keys(user.username)
        self.app.wd.find_element_by_name("pass").clear()
        self.app.wd.find_element_by_name("pass").send_keys(user.password)
        self.app.wd.find_element_by_css_selector("input[value='Login']").click()

    def logout(self):
        # Logout
        self.app.wd.find_element_by_link_text("Logout").click()