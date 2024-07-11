import time

from data import User
from conftest import driver
from locators import MainPageLocators, AuthorizationPageLocators, RegistrationPageLocators
from data import URLS
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_login_by_login_button_success(self, driver):
        # Вход в личный кабинет через кнопку "Войти"
        driver.get(URLS.MAIN_PAGE)
        driver.find_element(*MainPageLocators.login_account_but).click()
        driver.find_element(*AuthorizationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthorizationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthorizationPageLocators.login_account_auth_form_but).click()


        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(MainPageLocators.place_an_order_but))
        order_but = driver.find_element(*MainPageLocators.place_an_order_but).text

        assert (driver.current_url == URLS.MAIN_PAGE) and (order_but == 'Оформить заказ')

    def test_login_by_personal_account_button_success(self, driver):  # Вход в личный кабинет на Главной странице
        driver.get(URLS.MAIN_PAGE)
        driver.find_element(*MainPageLocators.personal_account_but).click()
        driver.find_element(*AuthorizationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthorizationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthorizationPageLocators.login_account_auth_form_but).click()

        WebDriverWait(driver, 25).until(ec.visibility_of_element_located(MainPageLocators.place_an_order_but))
        order_but = driver.find_element(*MainPageLocators.place_an_order_but).text

        assert (driver.current_url == URLS.MAIN_PAGE) and (order_but == 'Оформить заказ')

    def test_login_by_registration_form_success(self, driver):  # Вход в личный кабинет
        driver.get(URLS.REGISTRATION_PAGE)
        driver.find_element(*RegistrationPageLocators.enter_but).click()
        driver.find_element(*AuthorizationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*AuthorizationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*AuthorizationPageLocators.login_account_auth_form_but).click()

        WebDriverWait(driver, 25).until(ec.visibility_of_element_located(MainPageLocators.place_an_order_but))
        order_but = driver.find_element(*MainPageLocators.place_an_order_but).text

        assert (driver.current_url == URLS.MAIN_PAGE) and (order_but == 'Оформить заказ')
