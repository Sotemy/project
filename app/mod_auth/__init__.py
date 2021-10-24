from flask import Blueprint

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

from app.mod_auth import controllers
