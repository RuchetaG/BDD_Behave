from behave import *
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec

from Library import config_reader

from selenium.webdriver.support.wait import WebDriverWait


@given(u'User is on the login page')
def step_impl(context):
    context.driver.implicitly_wait(15)
    assert "Works" in context.driver.title


@when(u'User enters the username')
def step_impl(context):
    context.driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'username_css')).send_keys(
        config_reader.login_data_reader('login_data', 'username'))
    context.driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'username_continue_css')).click()


@when(u'User enters the "{password}"')
def step_impl(context, password):
    wait = WebDriverWait(context.driver, 20)
    element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, config_reader.elements_reader('Elements', 'password_css'))))
    context.driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'password_css')).send_keys(
        password)
    context.driver.find_element_by_css_selector(config_reader.elements_reader('Elements', 'password_continue_css')).click()

@then(u'User should be logged into the system')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)

    element = wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, config_reader.elements_reader('Elements', 'create_patient_menu_css'))))
    assert "https://staging-emr.houseworksinc.co/dashboard" == context.driver.current_url
    print(context.driver.current_url)


@then(u'Error should be displayed')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)

    element = wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, '[role="alert"]')))
    error_message = context.driver.find_element_by_css_selector('[role="alert"]').text
    print(error_message)
    assert error_message == "Invalid password"
