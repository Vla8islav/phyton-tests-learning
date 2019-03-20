import pytest
from fixture.application import Application
from model.user import User

fixture = None


@pytest.fixture
def app(request):
    global fixture
    user = User("admin", "secret")
    if fixture is None:
        browser = request.config.getoption("--browser")
        url = request.config.getoption("--url")
        fixture = Application(browser, url)
        fixture.session.login(user)
    elif not fixture.is_valid():
        fixture = Application()

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
    parser.addoption("--url", action="store", default="http://localhost/addressbook/")
