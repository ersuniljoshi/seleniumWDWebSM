# Using appium webdriver to automate
from appium import webdriver
import pytest
import os


def pytest_addoption(parser):
    parser.addoption("--codexFile", action="store", default="web", help="my option: web")
    parser.addoption("--browser", action="store", default="chrome", help="my option: ff or chrome")


@pytest.fixture
def codexFile(request):
    return request.config.getoption("--codexFile")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="function")
def setUpWeb(browser):
    desired_caps = {}
    desired_caps['platformName'] = 'Linux'
    desired_caps['platformVersion'] = '56.0.2924.87'
    desired_caps['browserName'] = browser
    driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)
    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
                if os.path.exists("myfile1"):
                        file = open('myfile1', 'r')
                        screenshot = file.read()
                        os.remove("myfile1")
                        extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))
        report.extra = extra
