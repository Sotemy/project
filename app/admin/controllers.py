from flask.templating import render_template
from app.admin import admin

@admin.route('/')
def showPanel():
    return render_template('admin/admin.html')