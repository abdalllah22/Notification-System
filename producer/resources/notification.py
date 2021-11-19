from flask import jsonify
from flask_restful import Resource, reqparse
from models.notification import NotificationModel
from helpers.rabitmq import send_msg


class Notification(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument('providers',
                        type=list,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('body',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    
    parser.add_argument('receivers',
                        type=list,
                        required=True,
                        help="This field cannot be blank."
                        )
    
    def post(self):
        
        data = Notification.parser.parse_args()
        
        notification = NotificationModel(data['providers'], data['body'], data['receivers'])
        # print(notification.id)
        try:
            notification.save_to_db()
            send_msg(notification.id)
        except:
            return {"message": "An error occurred sending the notification."}, 500

        return {"message": "Notification sended successfully."}, 201

    
    def get(self):
        return {'Notifications': list(map(lambda x: x.json(), NotificationModel.query.all()))}
        
