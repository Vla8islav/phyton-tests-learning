from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.dbfixture import DbFixture
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.generic_elements import GenericElementsHelper


class Application:

    def __init__(self, browser="firefox", url="http://localhost/addressbook/"):
        self.app_url = url
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.ie
        else:
            raise ValueError("Unrecognised browser option %s" % browser)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
        self.ge = GenericElementsHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_page_relative(self, right_part_of_url):
        if '/' == right_part_of_url[0]:
            right_part_of_url = right_part_of_url[1:]
        if '/' != self.app_url[-1]:
            self.app_url = "%s%s" % (self.app_url, '/')
        self.wd.get("%s%s" % (self.app_url, right_part_of_url))

    def open_home_page(self):
        # Open home page
        self.open_page_relative("/index.php")
        self.wd.refresh()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
