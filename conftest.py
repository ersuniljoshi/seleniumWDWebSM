# Using appium webdriver to automate
from selenium import webdriver
import pytest
import os


def pytest_addoption(parser):
    parser.addoption("--codexFile", action="store", default="web", help="my option: web")
    parser.addoption("--browser", action="store", default="chrome", help="my option: firefox or chrome")
    parser.addoption("--mode", action="store", default="local", help="mode: local or grid")
    parser.addoption("--platformName", action="store", default="Linux", help="name: Linux")
    parser.addoption("--platformVersion", action="store", default="55.0", help="version: 55.0")


@pytest.fixture
def codexFile(request):
    return request.config.getoption("--codexFile").lower()


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser").lower()

@pytest.fixture
def mode(request):
    return request.config.getoption("--mode").lower()

@pytest.fixture
def platformName(request):
    return request.config.getoption("--platformName").lower()

@pytest.fixture
def platformVersion(request):
    return request.config.getoption("--platformVersion")

@pytest.fixture(scope="function")
def setUpWeb(browser,mode,platformName,platformVersion):
    if mode == 'local':
        if browser == 'chrome':
            #chromedriver = "/usr/local/bin/chromedriver"
            #driver = webdriver.Chrome(chromedriver)
            driver = webdriver.Chrome()
            driver.maximize_window()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
            driver.maximize_window()
        else:
            print "no specified browser"
        return driver
    elif mode == 'grid':
        desired_caps = {}
        desired_caps['platformName'] = platformName
        desired_caps['platformVersion'] = platformVersion
        desired_caps['browserName'] = browser
        driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)
        return driver
    else:
        print "no mode"



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
