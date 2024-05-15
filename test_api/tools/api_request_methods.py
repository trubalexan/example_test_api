import requests


def request_api_get(url='', headers='', data='', json=''):
    """
    Метод выполняет GET запрос по указанному адресу, с передачей нужных параметров и возращает ответ от сервера
    :param url:
    :param headers:
    :param data:
    :param json:
    :return: api_response
    """
    api_response = requests.get(url=url, headers=headers, data=data, json=json)
    # print(api_response.json())
    return api_response


def request_api_post(url='', headers='', data='', json=''):
    """
    Метод выполняет POST запрос по указанному адресу, с передачей нужных параметров и возращает ответ от сервера
    :param url:
    :param headers:
    :param data:
    :param json:
    :return: api_response
    """
    api_response = requests.post(url=url, headers=headers, data=data, json=json)
    # print(api_response.json())
    return api_response


def request_api_delete(url='', headers='', data='', json=''):
    """
    Метод выполняет DELETE запрос по указанному адресу, с передачей нужных параметров и возращает ответ от сервера
    :param url:
    :param headers:
    :param data:
    :param json:
    :return: api_response
    """
    api_response = requests.delete(url=url, headers=headers, data=data, json=json)
    # print(api_response.json())
    return api_response


def request_api_patch(url='', headers='', data='', json=''):
    """
    Метод выполняет PATCH запрос по указанному адресу, с передачей нужных параметров и возращает ответ от сервера
    :param url:
    :param headers:
    :param data:
    :param json:
    :return: api_response
    """
    api_response = requests.patch(url=url, headers=headers, data=data, json=json)
    # print(api_response.json())
    return api_response


def request_api_put(url='', headers='', data='', json=''):
    """
    Метод выполняет PUT запрос по указанному адресу, с передачей нужных параметров и возращает ответ от сервера
    :param url:
    :param headers:
    :param data:
    :param json:
    :return: api_response
    """
    api_response = requests.put(url=url, headers=headers, data=data, json=json)
    # print(api_response.json())
    return api_response


def request_endpoint(api_url: str, param: dict):
    """
    Метод выполняет запрос по указанному адресу с указанными параметрами и возвращает ответ от сервера или None
    :param api_url:
    :param param:
    :return: endpoint_response or None
    """
    link = param["link"]
    link_extension = param["link_extension"]
    headers = param["header"]
    data = param["data"]
    json = param["json"]
    full_url = api_url + link + link_extension
    print("Отсылка запроса:\t", param["api_method"], ":", full_url)
    try:
        if param["api_method"] == 'get':
            endpoint_response = request_api_get(url=full_url, headers=headers, data=data, json=json)
        elif param["api_method"] == 'post':
            endpoint_response = request_api_post(url=full_url, headers=headers, data=data, json=json)
        elif param["api_method"] == 'delete':
            endpoint_response = request_api_delete(url=full_url, headers=headers, data=data, json=json)
        elif param["api_method"] == 'patch':
            endpoint_response = request_api_patch(url=full_url, headers=headers, data=data, json=json)
        elif param["api_method"] == 'put':
            endpoint_response = request_api_put(url=full_url, headers=headers, data=data, json=json)
        else:
            raise Exception(f'неизвестный код запроса: {param["api_method"]}')
        status = endpoint_response.status_code
        print(f'Проверка {link} с адресом {full_url}:\n'
              f'ожидаемый->полученный статус код {param["response_code"]}'
              f'->{status}')
        return endpoint_response
    except Exception as ex:
        print('Возникла ошибка:\t', ex)
        return None


def api_endpoint_request(api_endpoint_url: str, request_data: dict):
    """
    Метод выполняет запрос по указанному адресу с указанными параметрами, производит проверку на соответствие данных
    и возвращает ответ от сервера
    :param api_endpoint_url:
    :param request_data:
    :return: api_endpoint_answer
    """
    api_endpoint_answer = request_endpoint(api_endpoint_url, request_data)
    assert api_endpoint_answer is not None, f"Произошла ошибка при проверке {request_data['link']}"
    assert api_endpoint_answer.status_code == request_data["response_code"], \
        f"запрос {request_data['link']} выполнился с ошибкой: {api_endpoint_answer.json()}"
    if request_data["responses"] is not None:
        from tools.response_checks import response_json_compare
        responses_check = response_json_compare(request_data["responses"], api_endpoint_answer.json())
        assert not responses_check, f"Ошибка при сравнении данных ответа:\t{responses_check}"
    return api_endpoint_answer
