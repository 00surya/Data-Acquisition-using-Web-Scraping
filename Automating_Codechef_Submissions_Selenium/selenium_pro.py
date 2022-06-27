'''
selenium is a tool for automating task on web browser.....Written in using java but we have its python binding as well, that's  why  we can use it from python code as well.


Task - Automatically submit the code for a problem on codechef.

-To install python binding for selenium
    :pip install selenium
-To install webdriver

    :http://selenium-python.readthedocs.io/installation.html#drivers
    or
    pip install webdriver-manager---- 
    for example>>>>
                from selenium import webdriver
                from webdriver_manager.chrome import ChromeDriverManager

                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.get("https://www.google.com/")

''' 

from selenium import webdriver


browser = webdriver.Chrome("T:\dataScience\Data_Acquisition_01\Automating_Codechef_Submissions_Selenium\chromedriver_win32 (1)\chromedriver.exe")

browser.get('https://codechef.com')

username_element = browser.find_element_by_id("edit-name")
username_element.send_keys('snehill')

password_element = browser.find_element_by_id("edit-pass")
from getpass import getpass
password_element.send_keys(getpass("enter password"))
# password_element.send_keys('090#@nkK')

browser.find_element_by_id("edit-submit").click()

browser.get('https://www.codechef.com/submit/TEST')
browser.find_element_by_id('edit_area_toggle')

# language = browser.find_element_by_id('edit-language')
# language.send_keys('Python3(python  3.6)')



# with open("solution.cpp", 'r') as f:
    # code = f.read()


# code_element = browser.find_element_by_id('edit-program')
# code_element.send_keys(code)

browser.find_elements_by_css_selector('input#problem_code').value = 'Python3(python 3.6)'
# browser.find_elements_by_id("edit-submit").click()