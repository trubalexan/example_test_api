import requests
from settings import DOCS_URL_EXTENSION_v2, SCHEMA_URL_v2, DOCS_URL_EXTENSION_v3, SCHEMA_URL_v3
from data.data_docs import *
from tools.api_request_methods import api_endpoint_request
from tools.check_data import CompareData
from tools.schema_tools import gather_api_endpoints_method_names


def test_docs_page(testurl):
    """
    Тест проверяет доступность страниц апи документации
    :param testurl:
    :return:
    """
    print('\n---- Проверка доступа к странице документации проекта v2 ----')
    link_for_test = testurl + DOCS_URL_EXTENSION_v2
    print('Checking access for:\t' + link_for_test)
    response = requests.get(link_for_test)
    assert response.status_code == 200, "Ошибка при обработке запроса, неправильный статус код"
    assert "<title>Swagger UI</title>" in response.text, "Неправильный заголовок страницы"
    print('\n---- Проверка доступа к странице документации проекта v3 ----')
    link_for_test = testurl + DOCS_URL_EXTENSION_v3
    print('Checking access for:\t' + link_for_test)
    response = requests.get(link_for_test)
    assert response.status_code == 200, "Ошибка при обработке запроса, неправильный статус код"
    assert "<title>Swagger UI</title>" in response.text, "Неправильный заголовок страницы"
    print('\n---- Проверка закончена ----')


def test_openapi_page(testurl):
    """
    Test equality of API endpoints and methods to the reference list from data/data_docs.py
    :param testurl:
    :return:
    """
    print('\n---- Проверка страницы документации проекта в формате json: swagger_page v2 ----')
    openapi_answer = api_endpoint_request(SCHEMA_URL_v2, SWAGGER_v2)
    assert openapi_answer.json()["info"]["title"] == "Sample REST API", "Ошибка открытия, неправильный заголовок"
    endpoints = openapi_answer.json()["paths"]
    endpoints_method_list = gather_api_endpoints_method_names(endpoints)
    check_endpoints = CompareData(endpoints_method_list, ID_FULL_LIST_v2, ID_FULL_LIST_v2)
    check_status, check_results = check_endpoints.get_results()
    assert check_status, f"Разница в количества апи методов {check_results}"
    print("---- Список апи методов совпадает с требованиями ----")
    print('\n---- Проверка страницы документации проекта в формате json: openapi_page v3----')
    openapi_answer = api_endpoint_request(SCHEMA_URL_v3, OPENAPI_v3)
    assert openapi_answer.json()["info"]["title"] == "Sample REST API", "Ошибка открытия, неправильный заголовок"
    endpoints = openapi_answer.json()["paths"]
    endpoints_method_list = gather_api_endpoints_method_names(endpoints)
    check_endpoints = CompareData(endpoints_method_list, ID_FULL_LIST_v3, ID_FULL_LIST_v3)
    check_status, check_results = check_endpoints.get_results()
    assert check_status, f"Разница в количества апи методов {check_results}"
    print("---- Список апи методов совпадает с требованиями ----")
    print('\n---- Проверка закончена ----')



