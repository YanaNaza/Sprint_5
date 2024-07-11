import pytest
from selenium import webdriver
from locators import MainPageLocators, AuthorizationPageLocators
from data import URLS, User



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def get_login_driver(driver):
    driver.get(URLS.MAIN_PAGE)
    driver.find_element(*MainPageLocators.personal_account_but).click()
    driver.find_element(*AuthorizationPageLocators.email_input).send_keys(User.email)
    driver.find_element(*AuthorizationPageLocators.password_input).send_keys(User.password)
    driver.find_element(*AuthorizationPageLocators.login_account_auth_form_but).click()



