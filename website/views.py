from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    url_for
    )

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')