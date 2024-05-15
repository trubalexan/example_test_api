from tools.api_request_methods import request_endpoint
from data.data_single_user import *


def check_user_api_success(test_url_link: str, user_id: dict):
    """
    Тест проверяет работу запроса данных пользователя по его коду
    :param user_id:
    :param test_url_link:
    :return: api_single_user_answer
    """
    print('\n---- Проверка АПИ запроса данных пользователя по его коду ----')
    api_single_user_answer = request_endpoint(test_url_link, user_id)
    assert api_single_user_answer is not None, f"Произошла ошибка при проверке {user_id['link']}"
    addresses_status_code = api_single_user_answer.status_code
    assert addresses_status_code == user_id["response_code"], \
        f" не удалось получить данные пользователя: {api_single_user_answer.json()}"
    assert api_single_user_answer.json()["isSuccess"] == True, \
        f' получен ответ с ошибкой - {api_single_user_answer.json()["errorMessage"]}'
    print(" информация о пользователе: ", api_single_user_answer.json()["user"])
    print('\n---- Проверки закончены ----')
    return api_single_user_answer


def check_user_api_false_success_null(test_url_link: str, user_id: dict):
    """
    Тест проверяет работу запроса данных пользователя по его коду
    :param user_id:
    :param test_url_link:
    :return: api_single_user_answer
    """
    print('\n---- Проверка АПИ запроса данных пользователя по его коду ----')
    api_single_user_answer = request_endpoint(test_url_link, user_id)
    assert api_single_user_answer is not None, f"Произошла ошибка при проверке {user_id['link']}"
    addresses_status_code = api_single_user_answer.status_code
    assert addresses_status_code == user_id["response_code"], \
        f" не удалось получить данные пользователя: {api_single_user_answer.json()}"
    assert api_single_user_answer.json()["isSuccess"] == False, \
        f' получен ответ без ошибки - {api_single_user_answer.json()["errorMessage"]}'
    assert "NumberFormatException" in api_single_user_answer.json()["errorMessage"], \
        f' получен ответ без ошибки - {api_single_user_answer.json()["errorMessage"]}'
    print(" информация о пользователе: ", api_single_user_answer.json()["user"])
    print('\n---- Проверки закончены ----')
    return api_single_user_answer


def check_user_api_no_success(test_url_link: str, user_id: dict):
    """
    Тест проверяет работу запроса данных пользователя по его коду
    :param user_id:
    :param test_url_link:
    :return: api_single_user_answer
    """
    print('\n---- Проверка АПИ запроса данных пользователя по его коду ----')
    api_single_user_answer = request_endpoint(test_url_link, user_id)
    assert api_single_user_answer is not None, f"Произошла ошибка при проверке {user_id['link']}"
    addresses_status_code = api_single_user_answer.status_code
    assert addresses_status_code != 200, \
        f" удалось получить данные пользователя: {api_single_user_answer.json()}"
    if "errorMessage" in api_single_user_answer.json().keys():
        print(" информация: ", api_single_user_answer.json()["errorMessage"])
    print('\n---- Проверки закончены ----')
    return api_single_user_answer


def test_user_5(testurl: str):
    test_user_5_answer = check_user_api_success(testurl, USER_ID_5)
    assert test_user_5_answer.json()["user"] is not None, \
        " получен пустой список"
    assert test_user_5_answer.json()["user"]["id"] == 5, \
        " получен не правильный номер"
    assert test_user_5_answer.json()["user"]["name"] == "Ann", \
        " получено не правильное имя"
    assert test_user_5_answer.json()["user"]["gender"] == "female", \
        " получен не правильный гендер"
    assert test_user_5_answer.json()["user"]["age"] == 22, \
        " получен не правильный возраст"
    assert test_user_5_answer.json()["user"]["city"] == "Novosibirsk", \
        " получен не правильный город"


def test_user_minus_25(testurl: str):
    user_id_minus_25 = USER_ID_5
    user_id_minus_25["link_extension"] = "-25"
    test_user_minus_25_answer = check_user_api_success(testurl, user_id_minus_25)
    assert test_user_minus_25_answer.json()["user"] is None, \
        " получен не пустой список"


def test_user_645789(testurl: str):
    user_id_645789 = USER_ID_5
    user_id_645789["link_extension"] = "645789"
    check_user_api_success(testurl, user_id_645789)


def test_user_2147483647(testurl: str):
    user_id_2147483647 = USER_ID_5
    user_id_2147483647["link_extension"] = "2147483647"
    check_user_api_success(testurl, user_id_2147483647)


def test_user_minus_645789(testurl: str):
    user_id_minus_645789 = USER_ID_5
    user_id_minus_645789["link_extension"] = "-645789"
    check_user_api_success(testurl, user_id_minus_645789)


def test_user_minus_2147483648(testurl: str):
    user_id_minus_2147483648 = USER_ID_5
    user_id_minus_2147483648["link_extension"] = "-2147483648"
    check_user_api_success(testurl, user_id_minus_2147483648)


def test_user_2147483648(testurl: str):
    user_id_2147483648 = USER_ID_NOT_EXISTS
    user_id_2147483648["link_extension"] = "2147483648"
    check_user_api_false_success_null(testurl, user_id_2147483648)


def test_user_minus_2147483649(testurl: str):
    user_id_minus_2147483649 = USER_ID_NOT_EXISTS
    user_id_minus_2147483649["link_extension"] = "-2147483649"
    check_user_api_false_success_null(testurl, user_id_minus_2147483649)


def test_user_0(testurl: str):
    user_id_0 = USER_ID_5
    user_id_0["link_extension"] = "0"
    test_user_0_answer = check_user_api_success(testurl, user_id_0)
    assert test_user_0_answer.json()["user"] is not None, \
        " получен не пустой список"


def test_user_1(testurl: str):
    user_id_1 = USER_ID_5
    user_id_1["link_extension"] = "1"
    test_user_1_answer = check_user_api_success(testurl, user_id_1)
    assert test_user_1_answer.json()["user"] is None, \
        " получен не пустой список"


def test_user_no_id(testurl: str):
    user_no_id = USER_ID_NOT_EXISTS
    user_no_id["link_extension"] = ""
    user_no_id["response_code"] = 404
    check_user_api_no_success(testurl, user_no_id)


def test_user_random(testurl: str):
    user_id_random = USER_ID_NOT_EXISTS
    user_id_random["link_extension"] = "random"
    check_user_api_no_success(testurl, user_id_random)


def test_user_specials(testurl: str):
    user_id_specials = USER_ID_NOT_EXISTS
    user_id_specials["link_extension"] = "!@=2143&^*"
    check_user_api_no_success(testurl, user_id_specials)
