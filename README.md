# Python web script using Selenium Webdriver

## Task Completed for Project
==========================
- SM web automation using selenium WD
- Created separate codex file for web
- Written script with two testcases in it.
  including sign-in and sign-out
  
## Userdefine Command Line Parameters/Options for project :
========================================================

--browser
    usage   : Run script on chrome/firefox
    options : "chrome", "firefox"
    default : "chrome"
    
--codexFile
    usage   : Automate android app or ios app
    options : "android", ios, web
    default : "android"
    
## Pytest built-in Command Line Parameters/Options for project :
=============================================================

--html
    usage  : Generate html report for test result
    option : Path-for-report-file
             In our case report will be generate in this path
             "/home/vishal/gitrepo/appiumDemo/Results/report.html" 

    
## Commmand to run script :
========================
   py.test --browser="chrome" --codexFile=web test-path 
           --html=path-for-report-file --junitxml=path-for-junit-file
   In our case :
   Command :
   * py.test -v -s /home/vishal/gitrepos/seleniumWDWebSM/testlink_web_demo.py
           --browser="chrome" --codexFile=web --junitxml=junit.xml
        --html=/home/vishal/gitrepos/seleniumWDWebSM/Results/report.html *
   
Flow :
======

   Git code -> Jenkins -> Selenium grid -> selenium Node -> Browser 
                  |
                  |
                TestLink   
     