from locators import MainPageLocators
from data import URLS
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestConstructor:
    def test_switch_to_bun_constr_success(self, driver):  # Проверка перехода к «Булкам» в конструкторе
        driver.get(URLS.MAIN_PAGE)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.list_of_sauces))
        driver.find_element(*MainPageLocators.list_of_sauces).click()
        driver.find_element(*MainPageLocators.list_of_buns).click()
        assert driver.find_element(*MainPageLocators.active_tab_in_constructor).text == 'Булки'

    def test_switch_to_sauces_constr_success(self, driver):  # Проверка перехода к «Соусам» в конструкторе
        driver.get(URLS.MAIN_PAGE)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.list_of_sauces))
        driver.find_element(*MainPageLocators.list_of_sauces).click()
        assert driver.find_element(*MainPageLocators.active_tab_in_constructor).text == 'Соусы'

    def test_switch_to_toppings_constr_success(self, driver):  # Проверка перехода к «Начинкам» в конструкторе
        driver.get(URLS.MAIN_PAGE)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.fillings_list))
        driver.find_element(*MainPageLocators.fillings_list).click()
        assert driver.find_element(*MainPageLocators.active_tab_in_constructor).text == 'Начинки'
