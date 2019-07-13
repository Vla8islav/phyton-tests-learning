from selenium import webdriver

from fixture.contact_group_relation import ContactGroupRelationHelper
from fixture.contact import ContactHelper
from fixture.dbfixture import DbFixture
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.generic_elements import GenericElementsHelper

from selenium import webdriver



class Application:

    def __init__(self, browser="firefox", url="http://localhost/addressbook/"):

        capabilities = {
            "browserName": "chrome",
            "version": "73.0",
            "enableVNC": True,
            "enableVideo": False
        }

        driver = webdriver.Remote(
            command_executor="http://192.168.88.77:4444/wd/hub",
            desired_capabilities=capabilities)
        self.app_url = url
        # if browser == "firefox":
        #     self.wd = webdriver.Firefox()
        # elif browser == "chrome":
        #     self.wd = webdriver.Chrome()
        # elif browser == "ie":
        #     self.wd = webdriver.ie
        # else:
        #     raise ValueError("Unrecognised browser option %s" % browser)
        self.wd = driver
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
        self.contact_group_relation = ContactGroupRelationHelper(self)
        self.ge = GenericElementsHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_page_relative(self, right_part_of_url):
        self.wd.get(self.get_absolute_url(right_part_of_url))

    def get_absolute_url(self, right_part_of_url):
        if '/' == right_part_of_url[0]:
            right_part_of_url = right_part_of_url[1:]
        if '/' != self.app_url[-1]:
            self.app_url = "%s%s" % (self.app_url, '/')
        return "%s%s" % (self.app_url, right_part_of_url)

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
