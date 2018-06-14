from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI',
                                                  'sqlite:////tmp/test.db')
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'
