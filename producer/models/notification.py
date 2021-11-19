from db import db



class NotificationModel(db.Model):
    __tablename__ = 'notification'

    id = db.Column(db.Integer(), primary_key=True)
    providers = db.Column(db.PickleType())
    body = db.Column(db.String(80))
    receivers = db.Column(db.PickleType())
    
    


    def __init__(self, providers, body, receivers ):
        self.providers = providers
        self.body = body
        self.receivers = receivers
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def json(self):
        return {'providers': self.providers, 'body': self.body, 'receivers': self.receivers }
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()