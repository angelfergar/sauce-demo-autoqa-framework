import pytest
from base.webdriver_factory import WebDriverFactory

@pytest.fixture()
def set_up():
    print("Running method level set up")
    yield
    print("Running method level tear down")

@pytest.fixture(scope="class")
def one_time_setUp(request, browser):
    print("Running one time set up")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tear down")

# Add an option to select the browser while executing the tests in the cmd
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
