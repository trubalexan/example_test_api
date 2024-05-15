"""
Set of data required for testing SWAGGER and OPENAPI doc pages
"""

SWAGGER_v2 = {
    'api_method': "get",
    'link': "",
    'link_extension': "",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    'response_code': 200,
    'responses': {"swagger": "2.0",
                  "tags": None,
                  "info": None,
                  "host": "hr-challenge.dev.tapyou.com",
                  "basePath": "/",
                  "paths": None,
                  "definitions": None
                  }
}

OPENAPI_v3 = {
    'api_method': "get",
    'link': "",
    'link_extension': "",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    'response_code': 200,
    'responses': {"openapi": "3.0.1",
                  "servers": None,
                  "info": None,
                  "paths": None,
                  "components": None
                  }
}

ENDPOINTS = ['/api/test/user/{id}',
             '/api/test/users'
             ]

ID_FULL_LIST_v2 = ['userUsingGET',
                   'usersUsingGET'
                   ]

ID_FULL_LIST_v3 = ['users',
                   'user'
                   ]
