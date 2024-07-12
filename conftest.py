import json
import pytest
import requests
from endpoints import Endpoints
from urls import Urls
from user_data import data_correct


@pytest.fixture(scope='function')
def get_token():
    token = requests.post(Urls.MAIN_URL + Endpoints.LOGIN, headers=Endpoints.headers,
                          data=json.dumps(data_correct))
    new_token = token.json()['accessToken']
    return new_token
