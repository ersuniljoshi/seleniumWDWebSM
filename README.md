# Python web script using Selenium Webdriver

## Task Completed for Project

1. SM web automation using selenium WD

2. Created separate codex file for web

3. Written script with two testcases in it, including sign-in and sign-out
  
## Userdefine Command Line Parameters/Options for project :

* --browser

    usage   : Run script on chrome/firefox
    
    options : "chrome", "firefox"
    
    default : "chrome"
    
* --codexFile

    usage   : Automate SM website
    
    options : web
    
    default : "web"
    
## Pytest built-in Command Line Parameters/Options for project :

* --html

    usage  : Generate html report for test result
    
    option : Path-for-report-file
             
## Commmand to run script :

   py.test --browser="chrome" --codexFile=web test-path --html=path-for-report-file --junitxml=path-for-junit-file