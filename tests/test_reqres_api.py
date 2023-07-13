import allure
import pytest
from pytest_voluptuous import S
from requests import Response
from allure import step
from schemas.reqres import list_users_schema

@allure.tag("api")
@allure.label('owner', 'Sevav')
@allure.title('Возвращение запрашиваемого номера страницы')
def test_get_users_page_number(reqres_api):

    with step("USER PAGE NUMBER REQUEST (API)"):
        response: Response = reqres_api.get(
            url='/api/users?page=2'
        )

    with step("USER PAGE NUMBER = 2 (API)"):
        assert response.status_code == 200
        assert response.json()["page"] == 2


@allure.tag("api")
@allure.label('owner', 'Sevav')
@allure.title('Количество пользователей на странице')
def test_get_users_on_page(reqres_api):

    with step("USER ON PAGE REQUEST (API)"):
        response: Response = reqres_api.get(
            url='/api/users?page=2'
        )
    per_page = response.json()["per_page"]
    data_len = len(response.json()["data"])

    with step("USERS COUNT ON PAGE (API)"):
        assert data_len == per_page == 6


@allure.tag("api")
@allure.label('owner', 'Sevav')
@allure.title('Валидация схемы ответа')
def test_get_users_validate(reqres_api):

    with step("USERS SCHEMA REQUEST (API)"):
        response: Response = reqres_api.get(
            url='/api/users'
        )

    with step("VALIDATE SCHEMA (API)"):
        assert S(list_users_schema) == response.json()


@allure.tag("api")
@allure.label('owner', 'Sevav')
@allure.title('Проверка доступности нескольких страниц')
@pytest.mark.parametrize("path_part", ["users", "cutomers", "products"])
def test_get_path(reqres_api, path_part):

    with step("OPEN PAGE URL REQUEST (API)"):
        response: Response = reqres_api.get(
            url=f"/api/{path_part}"
        )

    with step("PAGE IS OPEN (API)"):
        assert response.status_code == 200
