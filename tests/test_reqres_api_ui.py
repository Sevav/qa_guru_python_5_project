import allure
from requests import Response
from selene.support.shared import browser
from allure import step
from pages.main import single_resource, user_not_found, register_successful, login_successful, login_unsuccessful


@allure.tag("ui")
@allure.label('owner', 'Sevav')
@allure.title('Пользователь не найден')
def test_single_user_not_found(reqres_ui):

    with step("SINGLE USER NOT FOUND (API)"):
        response = reqres_ui.get(
            url='/api/users/26'
        )

    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in/')

    user_not_found(response.status_code)


@allure.tag("ui")
@allure.label('owner', 'Sevav')
@allure.title('Показан один ресурс')
def test_single_resourse(reqres_ui):

    with step("SINGLE <RESOURCE> (API)"):
        response: Response = reqres_ui.get(
            url='/api/unknown/2'
        )
        response_data = response.json()
        response_name = str(response.json()['data']['name'])

    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in')

    single_resource(response_data, response_name)


@allure.tag("ui")
@allure.label('owner', 'Sevav')
@allure.title('Регистрация пользователя с получением токена')
def test_login_successful_with_token(reqres_ui):

    with step("REGISTER REQUEST (API)"):
        response: Response = reqres_ui.post(
            url='/api/register',
            data={'email': 'eve.holt@reqres.in', 'password': 'pistol'}
        )
        response_token = str(response.json()['token'])

    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in')

    register_successful(response_token)


@allure.tag("ui")
@allure.label('owner', 'Sevav')
@allure.title('Успешная авторизация пользователя')
def test_login_successful(reqres_ui):

    with step("LOGIN REQUEST (API)"):
        response: Response = reqres_ui.post(
            url='/api/login',
            data={'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
        )
        response_token = str(response.json()['token'])

    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in')

    login_successful(response_token)


@allure.tag("ui")
@allure.label('owner', 'Sevav')
@allure.title('Ошибка авторизации если не был введен пароль')
def test_login_unsuccessful(reqres_ui):

    with step("LOGIN REQUEST (API)"):
        response: Response = reqres_ui.post(
            url='/api/login',
            data={'email': 'peter@klaven'}
        )
        response_error = str(response.json()['error'])

    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in')

    login_unsuccessful(response_error)