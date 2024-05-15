from tools.api_request_methods import *
from data.data_no_auth import *


def check_api_access(test_api_url, links_data):
    """
    Тест проверяет работу апи без авторизации
    :param test_api_url:
    :return:
    """
    error_list = {}
    print('\n---- Проверки АПИ запросов без авторизации ----')
    for i in range(len(links_data)):
        response = ''
        try:
            if EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["api_method"] == 'get':
                response = request_api_get(url=(test_api_url + EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["link"]))
            elif EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["api_method"] == 'post':
                response = request_api_post(
                    url=(test_api_url + EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["link"]))
            elif EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["api_method"] == 'delete':
                response = request_api_delete(
                    url=(test_api_url + EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["link"]))
            elif EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["api_method"] == 'patch':
                response = request_api_patch(
                    url=(test_api_url + EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["link"]))
            else:
                raise Exception(
                    f'неизвестный код запроса: {EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["api_method"]}')
            print(f'Проверка линка {links_data[i]}: {EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["link"]}: '
                  f'ожидаемый->полученный статус код {EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["response_code"]}'
                  f'->{response.status_code}')

            assert response.status_code == EXPECTED_ANSWERS_UNAUTHORIZED_v2[links_data[i]]["response_code"], \
                f"Ошибка при обработке запроса {links_data[i]}, неправильный статус код"
        except Exception as ex:
            if response:
                error_list[links_data[i]] = response.status_code
            else:
                error_list[links_data[i]] = ex
            print('Возникла ошибка:\t', ex)
            continue
    print('\n---- Проверки закончены ----')
    assert not error_list


def test_api_access_v2(testurl):
    """
    Test checking the access to the SWAGGER v2 web page
    """
    test_data_urls_v2 = list(EXPECTED_ANSWERS_UNAUTHORIZED_v2.keys())
    check_api_access(testurl, test_data_urls_v2)


def test_api_access_v3(testurl):
    """
    Test checking the access to the OPENAPI v3 web page
    """
    test_data_urls_v3 = list(EXPECTED_ANSWERS_UNAUTHORIZED_v3.keys())
    check_api_access(testurl, test_data_urls_v3)
