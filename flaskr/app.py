from flask import render_template, Blueprint, Flask

bp = Blueprint('main', __name__)

@bp.route('/')
def home():

    return render_template("home.hl")

@bp.route('/loggedIn')
def homeLoggedIn():

    return render_template("loggedIn.hl")

@bp.route('/signUp')
def homeSignUp():

    return render_template("home.hl")

@bp.route('/about')
def about():

    return render_template("about.hl")

app = Flask(__name__)
app.register_blueprint(bp)
app.add_url_rule('/', endpoint='home')
app.add_url_rule('/about', endpoint = 'about')
app.add_url_rule('/loggedIn', endpoint='loggedIn')
app.add_url_rule('/signUp', endpoint='signUp')