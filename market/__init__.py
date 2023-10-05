from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'db630b2997f5cf9c60277917'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
from market import models

