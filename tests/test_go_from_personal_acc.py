from locators import MainPageLocators, PersonalAccountLocators, AuthorizationPageLocators
from conftest import driver, get_login_driver
from data import URLS
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAcc:

    def test_go_to_pesonal_acc_from_main_page(self, driver, get_login_driver):
        # Проверка перехода в личный кабинет по клику на кнопку "Личный кабинет"
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(MainPageLocators.personal_account_but))
        driver.find_element(*MainPageLocators.personal_account_but).click()
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(PersonalAccountLocators.exit_but))
        save_button = driver.find_element(*PersonalAccountLocators.save_but).is_displayed()

    def test_go_from_personal_acc_to_constructor_by_click_on_constructor_button_success(self, driver, get_login_driver):
        # Проверка перехода в личный кабинет по клику на кнопку "Конструктор"
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(MainPageLocators.personal_account_but))
        driver.find_element(*MainPageLocators.personal_account_but).click()
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(PersonalAccountLocators.exit_but))
        driver.find_element(*PersonalAccountLocators.constructor_but).click()
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(MainPageLocators.place_an_order_but))
        order_button_main_page = driver.find_element(*MainPageLocators.place_an_order_but)

        assert driver.current_url == URLS.MAIN_PAGE and order_button_main_page.text == "Оформить заказ"

    def test_go_from_personal_acc_to_constr_by_click_on_logo_success(self, driver, get_login_driver):
        # Проверка перехода в личный кабинет по клику на логотип сайта
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(MainPageLocators.personal_account_but))
        driver.find_element(*MainPageLocators.personal_account_but).click()
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(PersonalAccountLocators.exit_but))
        driver.find_element(*PersonalAccountLocators.logo_but).click()
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(MainPageLocators.place_an_order_but))
        order_button_main_page = driver.find_element(*MainPageLocators.place_an_order_but)

        assert driver.current_url == URLS.MAIN_PAGE and order_button_main_page.text == "Оформить заказ"

    def test_logout_from_personal_acc_success(self, driver, get_login_driver):
        # Проверка выхода из личного кабинета
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(MainPageLocators.personal_account_but))
        driver.find_element(*MainPageLocators.personal_account_but).click()
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(PersonalAccountLocators.exit_but))
        driver.find_element(*PersonalAccountLocators.exit_but).click()
        WebDriverWait(driver, 50).until(ec.visibility_of_element_located(AuthorizationPageLocators.login_account_auth_form_but))
        login_button = driver.find_element(*AuthorizationPageLocators.login_account_auth_form_but)

        assert driver.current_url == URLS.LOGIN_PAGE and login_button.text == 'Войти'