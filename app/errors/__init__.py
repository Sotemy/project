from flask import Blueprint

mod_error=Blueprint('errors', __name__)

from app.errors import handlers