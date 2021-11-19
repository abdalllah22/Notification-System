# notifications service

## Installation&Run

run `python app.py`


## Usage Scenario

- send notification to a user or group of users
- notification have many providers ('sms', 'email', 'fcm')

so to complete this scenario we should follow these steps

- send `POST` request to  `/users` to create user
- send `POST` request to  `/notifications` to send a notification

User body
```json
{
    "name": "ahmed",
    "email": "ahmed.abdalllah22@gmail.com"
}
```
Notification body
```json
{
    "providers": ["sms", "fcm"],
    "body": "How You Doing ?!",
    "receivers": ["1"]
}
```


- when we send request to **producer service** which is responsible to save notification to DB and notify notification service via **rabitmq**  



