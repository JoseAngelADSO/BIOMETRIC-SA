from flask import Flask
from sqlalchemy.ext.declarative import SQLAlchemy
from flask_cors import CORS 

app = Flask(__name__)
app.config[SQLAlchemy]=''
SQLAlchemy(app)