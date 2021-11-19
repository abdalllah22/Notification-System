import requests
import json

url = "http://127.0.0.1:5000"



def test_create_notification():
    body = {
        "providers": ["fcm", "sms", "email"],
        "body": "Hope is dangerous thing",
        "receivers": ["1", "5", "7"]
    }
    
    response = requests.post(url+"/notifications", data=body)
    print(response.json()['message'])  # Notification sended successfully
    assert response.status_code == 201
    

test_create_notification()