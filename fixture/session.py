from selenium.common.exceptions import NoSuchElementException


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

    def ensure_login(self, user):
        if not self.are_we_logged_in():
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
            self.login(user)

    def logout(self):
        self.app.wd.delete_all_cookies()
        self.app.wd.refresh()

    def ensure_logout(self):
        if self.are_we_logged_in():
            self.logout()

    def are_we_logged_in(self):
        return len(self.app.wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, user):
        try:
            retval = self.app.wd.find_element_by_css_selector("form[name='logout'] b").text == "(" + user.login + ")"
        except NoSuchElementException:
            retval = False
        return retval
