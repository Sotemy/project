from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask import request
from flask_login import LoginManager

from config import config

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object(config['development'])

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

login_manager=LoginManager(app)

# Translates
babel = Babel(app)
# Sample HTTP error handling
from app.errors import mod_error as error_module
app.register_blueprint(error_module)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

from app.admin import admin as admin_module
app.register_blueprint(admin_module)


#babel sets locate for translates
@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()