from flask import render_template, Blueprint, request, redirect, url_for
from main.Model import Post
from main.main.form import PasscodeForm

main = Blueprint('main', __name__)


@main.route("/ashes", methods=['GET', 'POST'])
def ashes():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('ashes.html', posts=posts, page=page)


@main.route("/",  methods=['GET', 'POST'])
def index():
    form = PasscodeForm()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template("index.html", form=form)


@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/selfintro", methods=['GET', 'POST'])
def selfintro():
    return render_template('selfintro.html')


@main.route("/blinks", methods=['GET', 'POST'])
def blinks():
    return render_template('blinks.html')


@main.route("/eggs", methods=['GET', 'POST'])
def eggs():
    return render_template('eggs.html')

