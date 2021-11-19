import requests
import json

url = "http://127.0.0.1:5000"


def test_create_user():
    body = {
        "name": "Ali",
        "email": "ali@gmail.com"
    }
    response = requests.post(url + "/users",data=body)
    print(response.json()['message'])  # User created successfully.
    assert response.status_code == 201
    

test_create_user()