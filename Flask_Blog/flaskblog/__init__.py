from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='31e8bb3d6717b9ffd7dec65051fec227' #the three slashes are the relative ath so the site should get created in our project diractory along side our python modlule
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes