from random import randint

class User:
    user_name = 'Yana'
    email = 'ya1234@ya.ru'
    password = '123456'
    invalid_password = "12345"

class RandomUser:
    user_name = f'name{randint(0, 99)}'
    email = f'mail{randint(0, 99)}@yandex.ru'
    password = f'{randint(100, 999)}yana'

class URLS:
    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"  # URL главной страницы
    LOGIN_PAGE = "https://stellarburgers.nomoreparties.site/login"  # URL страницы входа
    REGISTRATION_PAGE = "https://stellarburgers.nomoreparties.site/register"  # URL страницы регистрации
    PERSONAL_ACCOUNT_PAGE = "https://stellarburgers.nomoreparties.site/account/profile"  # Страница личного кабинета
