from flask import render_template, Blueprint, Flask

bp = Blueprint('test', __name__)

@bp.route('/')
def test():

    return render_template("home.hl")

app = Flask(__name__)
app.register_blueprint(bp)
app.add_url_rule('/', endpoint='test')