import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://localhost/flask_project_db')
db = SQLAlchemy(app)

@app.route('/')
def hello_world():

    db.create_all()
    logging.info(db)
    return 'Hello World!'

@app.route('/create')
def create_person():
    person = Person('John Doe', 'john.doe@example.com')
    db.session.add(person)
    db.session.commit()

if __name__ == '__main__':
    app.run()
