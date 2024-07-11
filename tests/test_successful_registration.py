from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from data import User, RandomUser, URLS
from locators import RegistrationPageLocators, AuthorizationPageLocators


class TestRegistrationPage:

    def test_registration_success(self, driver):
        # Проверка регистрации  пользователя
        driver.get(URLS.REGISTRATION_PAGE)
        WebDriverWait(driver, 25).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_but))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomUser.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomUser.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(User.password)
        WebDriverWait(driver, 30).until(
            ec.element_to_be_clickable(RegistrationPageLocators.registration_but)
        ).click()
        driver.find_element(*RegistrationPageLocators.registration_but).click()

        # WebDriverWait(driver, 20).until(ec.element_to_be_clickable(*RegistrationPageLocators.registration_but)).click()

        WebDriverWait(driver, 25).until(
            ec.visibility_of_element_located(AuthorizationPageLocators.login_account_auth_form_but))
        login_button_displayed = driver.find_element(
            *AuthorizationPageLocators.login_account_auth_form_but).is_displayed()

        assert driver.current_url == URLS.LOGIN_PAGE and login_button_displayed

    def test_registration_incorrect_password_check_error(self, driver):
        # Проверка ввода пароля менее 6 символов при регистрации
        driver.get(URLS.REGISTRATION_PAGE)
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_but))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomUser.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomUser.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(User.invalid_password)
        driver.find_element(*RegistrationPageLocators.registration_but).click()
        WebDriverWait(driver, 15).until(
            ec.visibility_of_any_elements_located(RegistrationPageLocators.error_message_incorrect_pass))
        error = driver.find_element(*RegistrationPageLocators.error_message_incorrect_pass).text

        assert (error == 'Некорректный пароль') and (driver.current_url == URLS.REGISTRATION_PAGE)

    def test_double_registration_check_error(self, driver):
        # Проверка попытки повторной регистрации
        driver.get(URLS.REGISTRATION_PAGE)
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_but))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(User.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*RegistrationPageLocators.registration_but).click()
        WebDriverWait(driver, 15).until(
            ec.visibility_of_element_located(RegistrationPageLocators.error_message_double_register))
        error = driver.find_element(*RegistrationPageLocators.error_message_double_register).text

        assert (error == 'Такой пользователь уже существует') and (driver.current_url == URLS.REGISTRATION_PAGE)

    def test_double_registration_check_error(self, driver):
        # Проверка попытки повторной регистрации
        driver.get(URLS.REGISTRATION_PAGE)
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_but))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(User.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(User.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(User.password)
        driver.find_element(*RegistrationPageLocators.registration_but).click()
        WebDriverWait(driver, 15).until(
            ec.visibility_of_element_located(RegistrationPageLocators.error_message_double_register))
        error = driver.find_element(*RegistrationPageLocators.error_message_double_register).text

        assert (error == 'Такой пользователь уже существует') and (driver.current_url == URLS.REGISTRATION_PAGE)

        # проверка регистрации с пустыми полем ИМЯ

    def test_registration_without_name(self, driver):
        driver.get(URLS.REGISTRATION_PAGE)
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_but))
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomUser.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(RandomUser.password)
        driver.find_element(*RegistrationPageLocators.registration_but).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(RegistrationPageLocators.registration_but))

        assert driver.find_element(*RegistrationPageLocators.registration_but).text == 'Зарегистрироваться'
