from flask import render_template, request

from app.admin import admin
from app.admin.forms import AdvertisingForm


@admin.route('/', methods=['GET', 'POST'])
def showPanel():
    form = AdvertisingForm(request.form)
    if form.validate_on_submit():
        pass
    return render_template('admin/admin.html', form=form)