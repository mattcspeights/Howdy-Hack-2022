from flask import render_template, Blueprint, Flask

bp = Blueprint('test', __name__)

@bp.route('/')
def home():

    return render_template("home.hl")

@bp.route('/loggedIn')
def homeLoggedIn():

    return 
app = Flask(__name__)
app.register_blueprint(bp)
app.add_url_rule('/', endpoint='test')
app.add_url_rule('/benis', endpoint='test')