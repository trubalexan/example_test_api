import requests
from settings import DOCS_URL_EXTENSION, SCHEMA_URL
from data.data_docs import *
from tools.api_request_methods import api_endpoint_request
from tools.check_data import CompareData
from tools.schema_tools import gather_api_endpoints_method_names


def test_docs_page(testurl):
    """
    Тест проверяет доступность страницы апи документации
    :param testurl:
    :return:
    """
    print('\n---- Проверка доступа к странице документации проекта ----')
    link_for_test = testurl + DOCS_URL_EXTENSION
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
    print('\n---- Проверка страницы документации проекта в формате json: openapi_page ----')
    openapi_answer = api_endpoint_request(SCHEMA_URL, SWAGGER_v2)
    assert openapi_answer.json()["info"]["title"] == "Sample REST API", "Ошибка открытия, неправильный заголовок"
    endpoints = openapi_answer.json()["paths"]
    endpoints_method_list = gather_api_endpoints_method_names(endpoints)
    # assert len(endpoints_method_list) == len(ENDPOINTS_FULL_LIST), "не соответствие количества методов"
    check_endpoints = CompareData(endpoints_method_list, ID_FULL_LIST, ID_FULL_LIST)
    check_status, check_results = check_endpoints.get_results()
    assert check_status, f"Разница в количества апи методов {check_results}"
    print("---- Список апи методов совпадает с требованиями ----")
    print('\n---- Проверка закончена ----')



