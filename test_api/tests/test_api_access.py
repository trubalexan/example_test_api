from tools.api_request_methods import *
from data.data_no_auth import *

test_urls = list(EXPECTED_ANSWERS_UNAUTHORIZED.keys())


def test_api_access(testurl):
    """
    Тест проверяет работу апи без авторизации
    :param testurl:
    :return:
    """
    error_list = {}
    print('\n---- Проверки АПИ запросов без авторизации ----')
    for i in range(len(test_urls)):
        response = ''
        try:
            if EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["api_method"] == 'get':
                response = request_api_get(url=(testurl + EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["link"]))
            elif EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["api_method"] == 'post':
                response = request_api_post(url=(testurl + EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["link"]))
            elif EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["api_method"] == 'delete':
                response = request_api_delete(url=(testurl + EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["link"]))
            elif EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["api_method"] == 'patch':
                response = request_api_patch(url=(testurl + EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["link"]))
            else:
                raise Exception(f'неизвестный код запроса: {EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["api_method"]}')
            print(f'Проверка линка {test_urls[i]}: {EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["link"]}: '
                  f'ожидаемый->полученный статус код {EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["response_code"]}'
                  f'->{response.status_code}')

            assert response.status_code == EXPECTED_ANSWERS_UNAUTHORIZED[test_urls[i]]["response_code"], \
                f"Ошибка при обработке запроса {test_urls[i]}, неправильный статус код"
        except Exception as ex:
            if response:
                error_list[test_urls[i]] = response.status_code
            else:
                error_list[test_urls[i]] = ex
            print('Возникла ошибка:\t', ex)
            continue
    print('\n---- Проверки закончены ----')
    assert not error_list
