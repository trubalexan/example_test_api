"""
Set of data required for testing endpoint usersUsingGET
"""

USERS_MALE = {
    'api_method': "get",
    'link': "/api/test/users",
    'link_extension': "?gender=male",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    "response_code": 200,
    "responses": {
        "isSuccess": None,
        "errorCode": None,
        "errorMessage": None,
        "idList": None
        }
    }

USERS_FEMALE = {
    'api_method': "get",
    'link': "/api/test/users",
    'link_extension': "?gender=female",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    "response_code": 200,
    "responses": {
        "isSuccess": None,
        "errorCode": None,
        "errorMessage": None,
        "idList": None
        }
    }

USERS_ANY = {
    'api_method': "get",
    'link': "/api/test/users",
    'link_extension': "?gender=any",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    "response_code": 200,
    "responses": {
        "isSuccess": None,
        "errorCode": None,
        "errorMessage": None,
        "idList": None
        }
    }

USERS_ARBITRARY = {
    'api_method': "get",
    'link': "/api/test/users",
    'link_extension': "?gender=arbitrary",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    "response_code": 500,
    "responses": {
        "timestamp": None,
        "status": None,
        "error": None,
        "path": None,
        "message": None
        }
    }

USERS_NO_GENDER = {
    'api_method': "get",
    'link': "/api/test/users",
    'link_extension': "?gender=",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    "response_code": 500,
    "responses": {
        "timestamp": None,
        "status": None,
        "error": None,
        "path": None,
        "message": None
        }
    }

USERS_NUMBER = {
    'api_method': "get",
    'link': "/api/test/users",
    'link_extension': "?gender=8",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    "response_code": 500,
    "responses": {
        "timestamp": None,
        "status": None,
        "error": None,
        "path": None,
        "message": None
        }
    }

USERS_SYMBOL = {
    'api_method': "get",
    'link': "/api/test/users",
    'link_extension': "?gender=#%any#$!",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    "response_code": 500,
    "responses": {
        "timestamp": None,
        "status": None,
        "error": None,
        "path": None,
        "message": None
        }
    }

USERS_LONG = {
    'api_method': "get",
    'link': "/api/test/users",
    'link_extension': "?gender=Lorem ipsum dolor sit amet. Ut facilis vero sed corporis fuga non nihil autem. At "
                      "voluptates reiciendis et dolorem dolore sed nostrum adipisci. Est nemo labore id quam quae cum "
                      "velit reiciendis. Nam autem quae et rerum odit aut blanditiis ipsum ea illo nostrum ea galisum "
                      "sequi. Et quibusdam magni quo distinctio saepe quo reiciendis dolor non dolorem praesentium "
                      "sit numquam maiores qui dolores quas. Est animi nesciunt sed obcaecati numquam et voluptatem "
                      "cumque non deleniti reiciendis qui totam nisi. Nam quia exercitationem aut rerum illo et "
                      "consequatur labore qui rerum quibusdam sit labore natus. Aut dolores Quis rem rerum suscipit "
                      "est temporibus optio sed dolores vero est temporibus obcaecati.",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    "response_code": 500,
    "responses": {
        "timestamp": None,
        "status": None,
        "error": None,
        "path": None,
        "message": None
        }
    }

USERS_SPACE = {
    'api_method': "get",
    'link': "/api/test/users",
    'link_extension': "?gender=ma le",
    'header': {"accept": "application/json",
               "charset": "utf-8"
               },
    'data': {},
    'json': {},
    "response_code": 500,
    "responses": {
        "isSuccess": None,
        "errorCode": None,
        "errorMessage": None,
        "idList": None
        }
    }
