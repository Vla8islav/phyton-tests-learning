
from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.generic_elements import GenericElementsHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
        self.ge = GenericElementsHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        # Open home page
        self.wd.get("http://localhost/addressbook/index.php")
        self.wd.refresh()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

