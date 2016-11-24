import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://localhost/flask_project_db')
db = SQLAlchemy(app)

from models import *

@app.route('/')
def hello_world():
    return render_template(
       'index.html',
       persons=Person.query.all())

@app.route('/create')
def create_person():
    person = Person('John', '1234')
    db.session.add(person)
    db.session.commit()

if __name__ == '__main__':
    app.run()
