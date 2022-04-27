from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tasks import make_celery

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
celery = make_celery(app)


db = SQLAlchemy(app)

from routes import *
from models import *

if __name__ == '__main__':
    app.run(debug=True)