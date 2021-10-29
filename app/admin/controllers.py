from flask import render_template, request

from app.admin import admin
from app.admin.forms import AdvertisingForm
from app.mod_auth.models import User


@admin.route('/', methods=['GET', 'POST'])
def showPanel():
    form = AdvertisingForm(request.form)
    if form.validate_on_submit():
        pass

    user=User.query.order_by(User.id).all()
    return render_template('admin/admin.html', form=form, user=user)