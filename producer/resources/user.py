from flask_restful import Resource, reqparse
from models.user import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = User.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400

        user = UserModel(data['name'], data['email'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201