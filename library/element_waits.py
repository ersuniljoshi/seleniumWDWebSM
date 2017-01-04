from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from element_codexes import ElementCodex
from selenium.webdriver.common.by import By

wait_timeout = 10
poll_frequency = 0.2


class Waits():
    def __init__(self, driver, codexFile):
        self.driver = driver
        self.time_interval = 50
        self.ECO = ElementCodex(codexFile)

    def waitUntilElementLocated(self, driver, codex):
        '''
        It will wait until element is not located till tiem interval
        :param driver: webdriver
        :param codex: codex for element
        :return: true if element located O.W False
        '''
        codex_details = self.ECO.get_codex(codex)
        try:
            visible = self.ECO.isElementLocated(codex_details)
            WebDriverWait(driver, self.time_interval).until(visible)
        except TimeoutException:
            print "Unable to locate element"
            return False
        return True

    def wait_Notify_Window_Gone(self, driver):
        WebDriverWait(
            driver,
            wait_timeout, poll_frequency=poll_frequency).until(
            lambda driver: self.is_Notify_Window_Gone(driver))

    def is_Notify_Window_Gone(self, driver):
        '''
        Sometimes the latter two :"Notifier_Timeout","Notifier_Newversion"
        not appearing in page, so comments out until get confirm from dev.

        notify_codex =["Notifier_Loading","Notifier_Custom","Notifier_Saving",
        "Notifier_Error","Notifier_Timeout","Notifier_Newversion"]
        This is a revised version of the previous call, to get better performance
        by avoiding the reading codex files and re-initiate codex each time this
        func is called.
        '''

        notify_codex = [
            "notifier-loading",
            "notifier-saving",
            "notifier-error",
            "notifier-custom"]
        notify_window_gone = True
        for codex_name in notify_codex:
            try:
                v_style = driver.find_element(
                    By.ID, codex_name).get_attribute('style')
                # notify window is hidden as bottom: -px
                if (v_style == u'' or "bottom: -" in v_style) and notify_window_gone:
                    notify_window_gone = True
                else:
                    # it contains bottom: positive px, meaning
                    # notify window's showing
                    return False
            except:
                # http://docs.seleniumhq.org/exceptions/stale_element_reference.jsp
                notify_window_gone = True
        return True
