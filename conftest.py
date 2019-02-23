import pytest
from fixture.application import Application
from model.user import User


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(User("admin", "secret"))

    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
