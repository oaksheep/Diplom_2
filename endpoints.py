class Endpoints:
    CREATE_USER = '/api/auth/register'
    LOGIN = '/api/auth/login'
    CHANGE_USER_DATA = '/api/auth/user'
    DELETE_USER = '/api/auth/user'
    CREATE_ORDER = '/api/orders'
    GET_ORDERS = '/api/orders'
    headers = {"Content-Type": "application/json"}
