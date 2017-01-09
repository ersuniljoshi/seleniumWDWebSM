# Import question builder class
from library.question_types import QuestionBuilder
# Importing setlog file for logging purpose
from library.setlog import Logger
loggerObj = Logger()
logger = loggerObj.setLogger("logs")


# Testcase 1 : This testcase will sign-in and create survey with 4 questions
def test_createSurveyWithQuesAndSignOut(setUpWeb, codexFile):
    driver = setUpWeb
    driver.get("http://surveymonkey.com")
    driver.maximize_window()
    QB = QuestionBuilder(driver, codexFile)
    logger.info("Executing Testcase 1...........")
    logger.info("Signing in..........")

    # User sign in
    assert QB.userSignIn()
    # create survey
    rv = QB.createSurvey("survey 1")
    if not rv:
        logger.info("survey creation failed")
        QB.tearDown()
        assert rv
    else:
        logger.info("Survey created")

    # Question 1 : Single text question
    rv = QB.web_addSingleTextTypeOfQueUsingAddNextQueButton("SM web automaton demo")
    if not rv:
        logger.info("Failed to add single text type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added single text type of question")

    # Question 2 : Multiple choice question
    rv = QB.web_addMultipleChoiceTypeOfQueUsingAddNextQueButton("How often do you use SM?")
    if not rv:
        logger.info("Failed to add multiple choice type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added multiple choice type of question")

    # Question 3 : Dropdown question
    rv = QB.web_addDropDownTypeOfQueUsingAddNextQueButton("Did you get meaningful data from survey analysis?")
    if not rv:
        logger.info("Failed to add Dropdown type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added Dropdown type of question")
    # sign out
    logger.info("Signing out..........")
    rv = QB.signOutUserLogin()
    if not rv:
        logger.info("Testcase 1 failed")
    else:
        logger.info("successfully signout")
        logger.info("Testcase 1 passed")
    QB.tearDown()
    assert rv


# Testcase 2 : This testcase will sign-in and create blank survey and then sign out
def test_singInWithCreateSurveyAndSignOut(setUpWeb, codexFile):
    driver = setUpWeb
    driver.get("http://surveymonkey.com")
    driver.maximize_window()
    QB = QuestionBuilder(driver, codexFile)
    logger.info("Executing Testcase 2...........")
    logger.info("Signing in..........")

    # User sign in
    assert QB.userSignIn()

    # create survey
    rv = QB.createSurvey("survey 2")
    if not rv:
        logger.info("survey creation failed")
        QB.tearDown()
        assert rv
    else:
        logger.info("Survey created")

    # Question 1 : Single text question
    rv = QB.web_addSingleTextTypeOfQueUsingAddNextQueButton("SM web automaton demo")
    if not rv:
        logger.info("Failed to add single text type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added single text type of question")

        # sign out
    logger.info("Signing out..........")
    rv = QB.signOutUserLogin()
    if not rv:
        logger.info("Testcase 2 failed")
    else:
        logger.info("successfully signout")
        logger.info("Testcase 2 passed")
    QB.tearDown()
    assert rv
