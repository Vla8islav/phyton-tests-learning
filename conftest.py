import json
import os

import pytest
from fixture.application import Application
from model.user import User

fixture = None
target = None


def get_project_folder():
    return os.path.dirname(os.path.realpath(__file__))


def get_data_folder():
    return os.path.join(get_project_folder(), "data")


@pytest.fixture
def app(request):
    global fixture
    global target
    config_file_name = os.path.join(get_project_folder(), request.config.getoption("--target"))
    if target is None:
        with open(config_file_name) as config_file:
            target = json.load(config_file)

    user = User(target["login"], target["password"])
    if fixture is None or not fixture.is_valid():
        browser = request.config.getoption("--browser")
        url = target["baseUrl"]
        fixture = Application(browser, url)
        fixture.session.login(user)

    fixture.session.ensure_login(user)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
