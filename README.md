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

* --hub_url

    usage   : Run script on the remote url of the selenium hub

    options : "http://localhost:4444/wd/hub"

    default : "http://localhost:4444/wd/hub"

* --platformName

    usage   : Run script on the specified platform name

    options : "Linux"

    default : "Linux"

* --platformVersion

    usage   : Run script on the specified platform version

    options : "55.0 or 56.0.2924.87"

    default : "56.0.2924.87"

* --mode

    usage   : Run script on the local or grid

    options : "local or grid"

    default : "local"
    
## Pytest built-in Command Line Parameters/Options for project :

* --html

    usage  : Generate html report for test result
    
    option : Path-for-report-file
             
## Commmand to run script :

   py.test -v -s testfile --browser='chrome' --hub_url='hub_url/wd/hub'
   --mode='grid' --platformName='Linux' --platformVersion='55.0' --codexFile=web test-path --html=path-for-report-file --junitxml=path-for-junit-file