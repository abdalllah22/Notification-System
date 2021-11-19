from flask import Flask
from flask_restful import Api

from resources.user import User
from resources.notification import Notification


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zxzx1212@localhost/nana'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'abdalllah22'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()




api.add_resource(User, '/users')
api.add_resource(Notification, '/notifications')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)