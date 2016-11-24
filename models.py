from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<Name %r>' % self.name
