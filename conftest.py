import pytest
from fixture.application import Application
from model.user import User

fixture = None


@pytest.fixture
def app():
    global fixture
    user = User("admin", "secret")
    if fixture is None:
        fixture = Application()
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
