from tools.api_request_methods import *
from data.data_no_auth import *


def check_api_access(test_api_url, pages_data):
    """
    Тест проверяет работу апи без авторизации
    :param test_api_url:
    :param pages_data:
    :return:
    """
    error_list = {}
    test_data_pages = list(pages_data.keys())
    print('\n---- Проверки АПИ запросов без авторизации ----')
    for i in test_data_pages:
        response = ''
        try:
            if pages_data[i]["api_method"] == 'get':
                response = request_api_get(url=(test_api_url + pages_data[i]["link"]))
            elif pages_data[i]["api_method"] == 'post':
                response = request_api_post(
                    url=(test_api_url + pages_data[i]["link"]))
            elif pages_data[i]["api_method"] == 'delete':
                response = request_api_delete(
                    url=(test_api_url + pages_data[i]["link"]))
            elif pages_data[i]["api_method"] == 'patch':
                response = request_api_patch(
                    url=(test_api_url + pages_data[i]["link"]))
            else:
                raise Exception(
                    f'неизвестный код запроса: {pages_data[i]["api_method"]}')
            print(f'Проверка линка {i}: {pages_data[i]["link"]}: '
                  f'ожидаемый->полученный статус код {pages_data[i]["response_code"]}'
                  f'->{response.status_code}')

            assert response.status_code == pages_data[i]["response_code"], \
                f"Ошибка при обработке запроса {i}, неправильный статус код"
        except Exception as ex:
            if response:
                error_list[i] = response.status_code
            else:
                error_list[i] = ex
            print('Возникла ошибка:\t', ex)
            continue
    print('\n---- Проверки закончены ----')
    assert not error_list


def test_api_access_v2(testurl):
    """
    Test checking the access to the SWAGGER v2 web page
    """
    check_api_access(testurl, EXPECTED_ANSWERS_UNAUTHORIZED_v2)


def test_api_access_v3(testurl):
    """
    Test checking the access to the OPENAPI v3 web page
    """
    check_api_access(testurl, EXPECTED_ANSWERS_UNAUTHORIZED_v3)
