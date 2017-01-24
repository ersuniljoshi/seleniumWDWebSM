from element_waits import Waits
from element_codexes import ElementCodex


class QuestionBuilder():
    def __init__(self, driver, codexFile):
        self.driver = driver
        self.WO = Waits(self.driver, codexFile+"_codexes.txt")
        self.ECO = ElementCodex(codexFile+"_codexes.txt")

    def createSurvey(self, question_title="Default_survey"):
        '''
        It will create survey with given title
        :param question_title:  survey title
        :return: returns True if survey created successfully
        '''
        rv = self.waitForElement("createSurvey")
        if not rv:
            return rv
        ele = self.getWebElement("createSurvey")
        if not self.click_element(ele):
            return False
        rv = self.waitForElement("createNewSurvey")
        if not rv:
            return rv
        ele = self.getWebElement("createNewSurvey")
        if not self.click_element(ele):
            return False
        ele = self.getWebElement("createSurveyTitle")
        if not ele:
            return ele
        else:
            ele.clear()
            ele.send_keys(question_title)
        ele = self.getWebElement("createSurveyAfterTitleEntered")
        return self.click_element(ele)

    def tearDown(self):
        '''
        Shutdown webdriver session
        :return: None
        '''
        self.driver.quit()

    def click_element(self, ele):
        if ele:
            ele.click()
            return True
        else:
            return False

    def waitForElement(self, codex):
        '''
        Wait for element appearance
        :param codex: codex for eleement
        :return: return True if element found O.W. False
        '''
        rv = self.WO.waitUntilElementLocated(self.driver, codex)
        return rv

    def getWebElement(self, codex):
        '''
        Used to return web element object
        :param codex: codex for web element
        :return: returns element O.W  False
        '''
        codex_details = self.ECO.get_codex(codex)
        ele = self.ECO.getElement(self.driver, codex_details)
        if ele:
            return ele
        else:
            return False

    def signOutUserLogin(self):
        '''
        signout for user
        :return: True if successfully signout O.W False
        '''
        ele = self.getWebElement("clickNextToCollectResponses")
        if not self.click_element(ele):
            return False
        rv = self.waitForElement("wheelButtonForSignOut")
        if not rv:
            return rv
        ele = self.getWebElement("wheelButtonForSignOut")
        if not self.click_element(ele):
            return False
        rv = self.waitForElement("signOutButton")
        if not rv:
            return rv
        ele = self.getWebElement("signOutButton")
        return self.click_element(ele)

    def userSignIn(self):
        '''
        user sign in
        :return: returns true if successfully sign in O.W False
        '''
        rv = self.waitForElement("signInButton")
        if not rv:
            return rv
        ele = self.getWebElement("signInButton")
        ele.click()
        ele = self.getWebElement("userNameEntry")
        ele.clear()
        ele.send_keys("InfoBeansP")
        ele = self.getWebElement("passwordEntry")
        ele.clear()
        ele.send_keys("InfoBeans!@#")
        ele = self.getWebElement("signInWithCredentials")
        ele.click()
        return True

    def web_addNextQuestionClick(self):
        rv = self.waitForElement("addNextQuestionButton")
        if not rv:
            return rv
        ele = self.getWebElement("addNextQuestionButton")
        return self.click_element(ele)

    def web_getDropdownMenuForQues(self):
        rv = self.waitForElement("changeQuesTypeDropdownButton")
        if not rv:
            return rv
        ele = self.getWebElement("changeQuesTypeDropdownButton")
        return self.click_element(ele)

    def web_addSingleTextTypeOfQueUsingAddNextQueButton(self, question_title):
        rv = self.web_addNextQuestionClick()
        if not rv:
            return rv
        rv = self.web_getDropdownMenuForQues()
        if not rv:
            return rv
        ele = self.getWebElement("selectSingleTextQueUsingDropdown")
        if not self.click_element(ele):
            return False
        ele = self.getWebElement("enterQuesTitle")
        ele.send_keys(question_title)
        rv = self.web_saveAnyTypeOfQuestion()
        if not rv:
            return rv
        return True

    def web_addMultipleChoiceTypeOfQueUsingAddNextQueButton(self, question_title):
        self.WO.wait_Notify_Window_Gone(self.driver)
        rv = self.web_addNextQuestionClick()
        if not rv:
            return rv
        rv = self.waitForElement("enterQuesTitle")
        if not rv:
            return rv
        ele = self.getWebElement("enterQuesTitle")
        ele.send_keys(question_title)
        ele = self.getWebElement("multipleChoiceQueRow1")
        ele.send_keys("Regularly")
        ele = self.getWebElement("multipleChoiceQueRow2")
        ele.send_keys("Sometimes")
        ele = self.getWebElement("multipleChoiceQueRow3")
        ele.send_keys("Never Tried")
        rv = self.web_saveAnyTypeOfQuestion()
        if not rv:
            return rv
        return True

    def web_addDropDownTypeOfQueUsingAddNextQueButton(self, question_title):
        self.WO.wait_Notify_Window_Gone(self.driver)
        rv = self.web_addNextQuestionClick()
        if not rv:
            return rv
        rv = self.waitForElement("enterQuesTitle")
        if not rv:
            return rv
        ele = self.getWebElement("enterQuesTitle")
        ele.send_keys(question_title)
        ele = self.getWebElement("dropDownQueTypeRow1")
        ele.send_keys("Yes")
        ele = self.getWebElement("dropDownQueTypeRow2")
        ele.send_keys("No")
        rv = self.web_saveAnyTypeOfQuestion()
        if not rv:
            return rv
        return True

    def hideKeyboard(self):
        self.driver.hide_keyboard()

    def web_saveAnyTypeOfQuestion(self):
        ele = self.getWebElement("saveQuestion")
        if ele is None:
            return False
        else:
            return self.click_element(ele)
