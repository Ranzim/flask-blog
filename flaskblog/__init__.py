from flask import Flask

from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

app.config['SECRET_KEY'] = 'y7duja!sjdsajkbdjk@bk$$213u'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes