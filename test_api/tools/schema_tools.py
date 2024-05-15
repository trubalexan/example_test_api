
def gather_api_endpoints_method_names(openapi_json_paths: dict):
    """
    Собирает имена методов "operatialId" со страницы документации и возвращает список имён
    :param openapi_json_paths:
    :return: api_method_list
    """
    api_method_list = []
    for api_endpoints in openapi_json_paths:
        for rest_methods in openapi_json_paths[api_endpoints]:
            api_method_list.append(openapi_json_paths[api_endpoints][rest_methods]["operationId"])
    return api_method_list


if __name__ == "__main__":
    """
    Gather methods ID from the schema
    """
    from settings import SCHEMA_URL
    from tools.api_request_methods import request_api_get
    api_answer = request_api_get(SCHEMA_URL)
    endpoints_path = api_answer.json()["paths"]
    print(gather_api_endpoints_method_names(endpoints_path))