data_double = {
    "email": 'test_email_123@yandex.ru',
    "password": "password_123",
    "name": "Lidiia"
}
data_correct = {
    "email": 'test_email_123@yandex.ru',
    "password": "password_123",
}

data_negative = {
    "email": 'test_email_123123@yandex.ru',
    "password": "password_123",
}

data_without_email = {
    "email": '',
    "password": "password_123",
    "name": "Lidiia"
}

data_without_password = {
    "email": 'test_email_123@yandex.ru',
    "password": "",
    "name": "Lidiia"
}

data_without_name = {
    "email": 'test_email_123@yandex.ru',
    "password": "password_123",
    "name": ""
}

data_updated = {
    "email": 'test_email_123@yandex.ru',
    "password": "password_123",
    "name": "NotLidiia"
}


data_ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
}

data_not_ingredients = {
        "ingredients": []
    }

data_ingredients_bad = {
    "ingredients": ["60d3b41abdacab0026a733c6g", "609646e4dc916e00276b2870g"]
}
