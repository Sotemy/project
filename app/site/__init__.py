from flask import Blueprint

site=Blueprint('site', __name__, url_prefix='/')

from app.site import controllers