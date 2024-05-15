from settings import DOCS_URL_EXTENSION_v2, DOCS_URL_EXTENSION_v3

"""
Set of data required for testing api page and endpoints accessibility
"""

EXPECTED_ANSWERS_UNAUTHORIZED_v2 = {
    # Main API page
    'DOCS_URL': {"link": f"{DOCS_URL_EXTENSION_v2}",
                 "response_code": 200,
                 "api_method": 'get'},
    # qa-test-controller
    'USER_URL': {"link": "/api/test/user/1",
                 "response_code": 200,
                 "api_method": 'get'},

    'USERS_URL': {"link": "/api/test/users?gender=male",
                  "response_code": 200,
                  "api_method": 'get'},
}

EXPECTED_ANSWERS_UNAUTHORIZED_v3 = {
    # Main API page
    'DOCS_URL': {"link": f"{DOCS_URL_EXTENSION_v3}",
                 "response_code": 200,
                 "api_method": 'get'},
    # qa-test-controller
    'USER_URL': {"link": "/api/test/user/1",
                 "response_code": 200,
                 "api_method": 'get'},

    'USERS_URL': {"link": "/api/test/users?gender=male",
                  "response_code": 200,
                  "api_method": 'get'},
}
