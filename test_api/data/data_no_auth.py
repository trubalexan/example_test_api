"""
Set of data required for testing api page and endpoints accessibility
"""

EXPECTED_ANSWERS_UNAUTHORIZED = {
    # Main API page
    'DOCS_URL': {"link": "/swagger-ui.html?urls.primaryName=QA#/",
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
