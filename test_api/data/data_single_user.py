USER_ID_5 = {
    'api_method': "get",
    'link': "/api/test/user/",
    'link_extension': "5",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    'response_code': 200,
    'responses': {"isSuccess": None,
                  "errorCode": None,
                  "errorMessage": None,
                  "user": None}
}

USER_ID_NOT_EXISTS = {
    'api_method': "get",
    'link': "/api/test/user/",
    'link_extension': "",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    'response_code': 400,
    'responses': {"isSuccess": None,
                  "errorCode": None,
                  "errorMessage": None,
                  "user": None}
}
