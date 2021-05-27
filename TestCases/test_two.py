from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from Library import InitiateDriver
from Library import config_reader


def test_validate_login():
    global driver
    driver = InitiateDriver.startBrowser(config_reader.config_reader('Data', 'Browser'))
    assert "Works" in driver.title
    print(driver.title)
    driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'username_css')).send_keys(config_reader.login_data_reader('login_data', 'username'))
    driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'username_continue_css')).click()
    driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'password_css')).send_keys(config_reader.login_data_reader('login_data', 'password'))
    driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'password_continue_css')).click()

    wait = WebDriverWait(driver, 20)

    element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, config_reader.elements_reader('Elements', 'create_patient_menu_css'))))
    assert "https://staging-emr.houseworksinc.co/dashboard" == driver.current_url
    print(driver.current_url)


def test_open_patients_tab():
    driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'patient_menu_css')).click()
    driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'create_patient_menu_css')).click()

    assert "Create Patient" == driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'add_patient_title_css')).text
    InitiateDriver.closeBrowser()
