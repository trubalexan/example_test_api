import copy
import time

from data.data_single_user import USER_ID_5
from data.data_users import USERS_ANY
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


def test_data_format(testurl):
    """
    Test is checking that recieved user data has the proper format
    """
    user_format_data = copy.deepcopy(USER_ID_5)
    list_users_id = check_users_api_success(testurl, USERS_ANY).json()["idList"]
    format_error_list = {}
    for user_id in list_users_id:
        user_format_errors = {}
        try:
            user_format_data["link_extension"] = str(user_id)
            user_format_answer = check_user_api(testurl, user_format_data)
            data_format_json = user_format_answer.json()
            print(data_format_json)
            if data_format_json["isSuccess"] not in [True, False]:
                user_format_errors["isSeccess"] = "wrong format"
            if data_format_json["errorCode"] != 0:
                user_format_errors["errorCode"] = "wrong code"
            if data_format_json["errorMessage"] is not None:
                user_format_errors["errorMessage"] = data_format_json["errorMessage"]
            if not data_format_json["user"]:
                user_format_errors["user"] = "no user data"
            else:
                if not isinstance(data_format_json["user"]["id"], int):
                    user_format_errors["user_id"] = "wrong format"
                if not isinstance(data_format_json["user"]["name"], str):
                    user_format_errors["user_name"] = "wrong format"
                if data_format_json["user"]["gender"] not in ["male", "female", "magic", "McCloud"]:
                    user_format_errors["user_gender"] = "wrong format"
                if isinstance(data_format_json["user"]["age"], int):
                    if (data_format_json["user"]["age"] < 16) or (data_format_json["user"]["age"] > 100):
                        user_format_errors["user_age"] = f'wrong age {data_format_json["user"]["age"]}'
                else:
                    user_format_errors["user_age"] = "wrong format"
                if not isinstance(data_format_json["user"]["city"], str):
                    user_format_errors["user_city"] = "wrong format"
                reg_date_time_str = data_format_json["user"]["registrationDate"]
                # if len(reg_date_time_str) > 23:
                #     print(reg_date_time_str)
                #     reg_date_time_str = reg_date_time_str[:23]
                #     print(reg_date_time_str)
                # reg_len = len(reg_date_time_str)
                if len(reg_date_time_str) < 19:
                    user_format_errors["user_registrationDate"] = f"wrong format for {reg_date_time_str}"
                else:
                    if reg_date_time_str[4] == "-" and reg_date_time_str[7] == "-" and reg_date_time_str[10] == "T" \
                        and reg_date_time_str[13] == ":" and reg_date_time_str[16] == ":": # and reg_date_time_str[
                            # 19] == ".":
                        reg_year = int(reg_date_time_str[:4])
                        if (2000 > reg_year) or (reg_year > 2024):
                            user_format_errors["user_reg_year"] = f"wrong year {reg_year}"
                        reg_month = int(reg_date_time_str[5:7])
                        if (reg_month <= 0) or (reg_month > 12):
                            user_format_errors["user_reg_month"] = f"wrong month {reg_month}"
                        reg_day = int(reg_date_time_str[8:10])
                        if (reg_day <= 0) or (reg_day > 31):
                            user_format_errors["user_reg_day"] = f"wrong day {reg_day}"
                        reg_hour = int(reg_date_time_str[11:13])
                        if (reg_hour < 0) or (reg_hour > 24):
                            user_format_errors["user_reg_hour"] = f"wrong hours {reg_hour}"
                        reg_minute = int(reg_date_time_str[14:16])
                        if (reg_minute < 0) or (reg_minute > 59):
                            user_format_errors["user_reg_minute"] = f"wrong minutes {reg_minute}"
                        reg_seconds = float(reg_date_time_str[17:])
                        if (reg_seconds < 0) or (reg_seconds > 59.999):
                            user_format_errors["user_registrationDate"] = f"wrong seconds {reg_seconds}"
                    else:
                        user_format_errors["user_registrationDate"] = f"wrong format {reg_date_time_str}"
            assert not user_format_errors
        except Exception as ex:
            format_error_list[str(user_id)] = ex
            # print(ex)
    assert not format_error_list, f"Test finished with errors: {format_error_list}"
    print("Test finished with no errors")


def test_response_time(testurl):
    """
    Test is checking response time limit = 1 sec
    """
    user_format_data = copy.deepcopy(USER_ID_5)
    list_users_id = check_users_api_success(testurl, USERS_ANY).json()["idList"]
    time_limit_error_list = {}
    response_time_list = {}
    for user_id in list_users_id:
        try:
            user_format_data["link_extension"] = str(user_id)
            start_time = time.time_ns()
            check_user_api(testurl, user_format_data)
            stop_time = time.time_ns()
            response_time_list[user_id] = (stop_time - start_time) * 0.000000001
            if response_time_list[user_id] > 1:
                time_limit_error_list[user_id] = response_time_list[user_id]
        except Exception as ex:
            time_limit_error_list[str(user_id)] = ex
            # print(ex)
    print("время отклика:\t", response_time_list)
    assert not time_limit_error_list, f"Test finished with errors: {time_limit_error_list}"