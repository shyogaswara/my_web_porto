import random
import string
from flask import Flask

def create_app():
    global UPLOAD_FOLDER
    _str_ = string.ascii_lowercase
    _secret_key_ = ''.join(random.choice(_str_) for i in range(12))

    app = Flask(__name__)
    app.config['SECRET KEY'] = _secret_key_
    app.secret_key = _secret_key_
    app.config['MAX_CONTENT_LENGTH'] = 100*1024*1024

    #from .auth import auth
    from .views import views

    #app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    return app