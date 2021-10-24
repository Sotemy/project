from flask import render_template
from app.errors import mod_error

@mod_error.app_errorhandler(404)
def error404(error):
    return render_template('errors/404.html', error=error), 404

@mod_error.app_errorhandler(500)
def error404(error):
    return render_template('errors/500.html', error=error), 500
