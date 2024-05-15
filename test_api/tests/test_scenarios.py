import copy
from data.data_single_user import USER_ID_5
from tests.test_users import check_users_api_success
from tools.api_request_methods import request_endpoint
from tools.create_random_data import create_id_list


def check_user_api(test_url_link: str, user_data_with_id: dict):
    """
    Метод проверяет получение данных пользователя по его коду
    :param user_data_with_id:
    :param test_url_link:
    :return: api_user_answer
    """
    api_user_answer = request_endpoint(test_url_link, user_data_with_id)
    assert api_user_answer is not None, f"Произошла ошибка при проверке {user_data_with_id['link']}"
    addresses_status_code = api_user_answer.status_code
    assert addresses_status_code == user_data_with_id["response_code"], \
        f"{api_user_answer.json()}"
    return api_user_answer


def test_random_ids(testurl):
    """
    Тест проверяет получение данных пользователей по случайному коду
    :param testurl:
    :return:
    """
    list_of_ids = create_id_list()
    user_test_data = copy.deepcopy(USER_ID_5)
    error_list = {}
    for i in list_of_ids:
        # if i == 0:
        #     i = 1
        user_test_data["link_extension"] = str(i)
        try:
            check_user_api(testurl, user_test_data)
        except Exception as ex:
            error_list[str(i)] = ex

    assert not error_list, f"Test finished with errors: {error_list}"
    print("Test finished with no errors")


def check_users_correct_id(test_list_url, users_id_list):
    """
    Метод проверяет получение данных кодов пользователей согласно списку кодов
    :param test_list_url:
    :param users_id_list:
    :return: error_list
    """
    user_test_id_data = copy.deepcopy(USER_ID_5)
    error_list = {}
    for correct_id in users_id_list:
        user_test_id_data["link_extension"] = str(correct_id)
        try:
            check_user_id_answer = check_user_api(test_list_url, user_test_id_data)
            assert check_user_id_answer.json()["user"], \
                f' no user data present: {check_user_id_answer.json()["user"]}'
            user_answer_id = check_user_id_answer.json()["user"]["id"]
            assert user_answer_id == correct_id, \
                f" received user id: {user_answer_id}, does not match with requested {correct_id}"
        except Exception as ex:
            error_list[str(correct_id)] = ex
    return error_list


def check_users_list_gender(test_list_url, users_id_list, user_gender):
    """
    Метод проверяет получение данных пола пользователей согласно списку кодов
    :param user_gender:
    :param test_list_url:
    :param users_id_list:
    :return: error_list
    """
    user_test_data = copy.deepcopy(USER_ID_5)
    error_list = {}
    for i in users_id_list:
        user_test_data["link_extension"] = str(i)
        try:
            check_user_answer = check_user_api(test_list_url, user_test_data)
            assert check_user_answer.json()["user"], \
                f' no user data present: {check_user_answer.json()["user"]}'
            user_answer_gender = check_user_answer.json()["user"]["gender"]
            assert user_answer_gender in ["male", "female", "magic", "McCloud"], \
                f" unknown user gender: {user_answer_gender}"
            if user_gender:
                assert user_answer_gender == user_gender, \
                    f" received user gender: {user_answer_gender}, do not match with requested {user_gender}"
        except Exception as ex:
            error_list[str(i)] = ex
    return error_list


def test_users_any_exists(testurl):
    """
    Тест проверяет наличие пользователей по списку
    :param testurl:
    :return:
    """
    from data.data_users import USERS_ANY
    list_users_any = check_users_api_success(testurl, USERS_ANY).json()["idList"]
    any_user_test_data = copy.deepcopy(USER_ID_5)
    any_error_list = {}
    for any_user in list_users_any:
        any_user_test_data["link_extension"] = str(any_user)
        try:
            check_user_api(testurl, any_user_test_data)
        except Exception as ex:
            any_error_list[str(any_user)] = ex
    assert not any_error_list, f"Test finished with errors: {any_error_list}"
    print("Test finished with no errors")


def test_users_by_id(testurl):
    """
    Тест проверяет данные для списка пользователей по номеру
    :param testurl:
    :return:
    """
    from data.data_users import USERS_ANY
    list_users_by_id = check_users_api_success(testurl, USERS_ANY).json()["idList"]
    id_error_list = check_users_correct_id(testurl, list_users_by_id)
    assert not id_error_list, f"Test finished with errors: {id_error_list}"
    print("Test finished with no errors")


def test_users_gender_male(testurl):
    """
    Тест проверяет данные для списка пользователей мужского пола
    :param testurl:
    :return:
    """
    from data.data_users import USERS_MALE
    list_users_male = check_users_api_success(testurl, USERS_MALE).json()["idList"]
    male_error_list = check_users_list_gender(testurl, list_users_male, "male")
    assert not male_error_list, f"Test finished with errors: {male_error_list}"
    print("Test finished with no errors")


def test_users_gender_female(testurl):
    """
    Тест проверяет данные для списка пользователей женского пола
    :param testurl:
    :return:
    """
    from data.data_users import USERS_FEMALE
    list_users_female = check_users_api_success(testurl, USERS_FEMALE).json()["idList"]
    female_error_list = check_users_list_gender(testurl, list_users_female, "female")
    assert not female_error_list, f"Test finished with errors: {female_error_list}"
    print("Test finished with no errors")


def test_users_gender_any(testurl):
    """
    Тест проверяет данные для списка пользователей любого пола
    :param testurl:
    :return:
    """
    from data.data_users import USERS_ANY
    list_users_any = check_users_api_success(testurl, USERS_ANY).json()["idList"]
    any_error_list = check_users_list_gender(testurl, list_users_any, None)
    assert not any_error_list, f"Test finished with errors: {any_error_list}"
    print("Test finished with no errors")


def test_all_ids(testurl):
    """
    Test is checking the user response status code for the list of ids
    """
    all_users_test_data = copy.deepcopy(USER_ID_5)
    any_error_list = {}
    for any_user in range(200, 220):  # full range -2147483648, 2147483647 will take too much time
        all_users_test_data["link_extension"] = str(any_user)
        try:
            check_user_api(testurl, all_users_test_data)
        except Exception as ex:
            any_error_list[str(any_user)] = ex
    assert not any_error_list, f"Test finished with errors: {any_error_list}"
    print("Test finished with no errors")
