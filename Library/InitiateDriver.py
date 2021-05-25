import getpass
import time
import os
from webdrivermanager import GeckoDriverManager, ChromeDriverManager
from selenium import webdriver
from Library import config_reader


def startBrowser(Browser_name):
    global driver
    return_value = sending_browser_driver(Browser_name)
    path_of_driver = download_browser_driver(return_value)
    driver = choose_web_driver(Browser_name, path_of_driver)

    driver.get(config_reader.config_reader('Data', 'Application_URL'))
    driver.maximize_window()

    return driver


def sending_browser_driver(get_string):
    send_browser_driver = {
        "Chrome": "chromedriver.exe",
        "Firefox": "geckodriver.exe"
    }
    return send_browser_driver[get_string]


def select_driver(browser):
    chrome_driver = ChromeDriverManager()
    firefox_driver = GeckoDriverManager()
    if browser == "geckodriver.exe":
        return firefox_driver
    elif browser == "chromedriver.exe":
        return chrome_driver


def download_browser_driver(browser):
    user_name = getpass.getuser()

    new_path = r"C:\\Users\\" + user_name + r"\\bin"
    exe_path = r"C:\\Users\\" + user_name + r"\AppData\Local\rasjani\WebDriverManager\bin\\" + browser
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    for root, directory, files in os.walk(new_path):
        browser_driver = select_driver(browser)
        gdd = browser_driver
        gdd.download_and_install()

        from shutil import copyfile
        copyfile(exe_path, new_path + r"\\" + browser)

    return new_path + r"\\" + browser


def choose_web_driver(browser, driver_path):
    if browser == "Chrome":
        chrome_driver = webdriver.Chrome(executable_path=driver_path)
        return chrome_driver
    elif browser == "Firefox":
        firefox_driver = webdriver.Firefox(executable_path=driver_path)
        return firefox_driver


