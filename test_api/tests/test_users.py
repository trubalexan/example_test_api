from tools.api_request_methods import request_endpoint
from data.data_users import *


def check_users_api_success(test_url_link: str, user_type: dict):
    """
    Тест проверяет работу запроса пользователей
    :param user_type:
    :param test_url_link:
    :return: api_users_answer
    """
    print('\n---- Проверка АПИ запроса списка пользователей ----')
    api_users_answer = request_endpoint(test_url_link, user_type)
    assert api_users_answer is not None, f"Произошла ошибка при проверке {user_type['link']}"
    addresses_status_code = api_users_answer.status_code
    assert addresses_status_code == user_type["response_code"], \
        f" не удалось получить список пользователей: {api_users_answer.json()}"
    assert api_users_answer.json()["isSuccess"] == True, \
        f' получен ответ с ошибкой - {api_users_answer.json()["errorMessage"]}'
    assert api_users_answer.json()["idList"] != [], \
        " получен пустой список"
    print(" список номеров пользователей: ", api_users_answer.json()["idList"])
    print('\n---- Проверки закончены ----')
    return api_users_answer


def check_users_api_error(test_url_link: str, user_type: dict):
    """
    Метод проверяет работу запроса пользователей
    :param user_type:
    :param test_url_link:
    :return: api_users_answer
    """
    print('\n---- Проверка АПИ запроса списка пользователей с ошибкой ----')
    api_users_answer = request_endpoint(test_url_link, user_type)
    assert api_users_answer is not None, f"Произошла ошибка при проверке {user_type['link']}"
    addresses_status_code = api_users_answer.status_code
    assert addresses_status_code == user_type["response_code"], \
        f" удалось получить список пользователей: {api_users_answer.json()}"
    assert api_users_answer.json()["message"] is not None, \
        ' получен ответ без описания ошибки'
    assert api_users_answer.json()["error"] is not None, \
        " получен ответ без названия ошибки"
    print(" ответ вернул ошибку: ", api_users_answer.json()["message"])
    print('\n---- Проверки закончены ----')
    return api_users_answer


def test_users_male(testurl: str):
    """
    Тест проверяет ответ сервера при запросе данных пользователей мужского пола
    """
    check_users_api_success(testurl, USERS_MALE)


def test_users_female(testurl: str):
    """
    Тест проверяет ответ сервера при запросе данных пользователей женского пола
    """
    check_users_api_success(testurl, USERS_FEMALE)


def test_users_any(testurl: str):
    """
    Тест проверяет ответ сервера при запросе данных пользователей любого пола
    """
    check_users_api_success(testurl, USERS_ANY)


def test_users_arbitrary(testurl: str):
    """
    Тест проверяет ответ сервера при запросе данных пользователей несуществующего пола
    """
    check_users_api_error(testurl, USERS_ARBITRARY)


def test_users_no_gender(testurl: str):
    """
    Тест проверяет ответ сервера при запросе данных пользователей без указания пола
    """
    check_users_api_error(testurl, USERS_NO_GENDER)


def test_users_number(testurl: str):
    """
    Тест проверяет ответ сервера при запросе данных пользователей при отправке цифры вместо пола
    """
    check_users_api_error(testurl, USERS_NUMBER)


def test_users_symbol(testurl: str):
    """
    Тест проверяет ответ сервера при запросе данных пользователей при отправке спецсимволов вместо пола
    """
    check_users_api_error(testurl, USERS_SYMBOL)


def test_users_long(testurl: str):
    """
    Тест проверяет ответ сервера при запросе данных пользователей при отправке длинной строки вместо пола
    """
    check_users_api_error(testurl, USERS_LONG)


def test_users_space(testurl: str):
    """
    Тест проверяет ответ сервера при наличии пробела в названии пола пользователя
    """
    check_users_api_error(testurl, USERS_SPACE)
    USERS_SPACE["link_extension"] = "?gender= male"
    check_users_api_error(testurl, USERS_SPACE)
    USERS_SPACE["link_extension"] = "?gender=male "
    check_users_api_error(testurl, USERS_SPACE)
