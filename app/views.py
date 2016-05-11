from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [ # fake array of posts
        {
        'autor': {'nickname': 'John'},
        'body': 'Beautiful day in Portland!'
        },
        {
        'autor': {'nickname': 'Susan'},
        'body': 'The avengers movie was so cool!'
        },
        {
        'autor': {'nickname': 'Willian'},
        'body': 'Teu cu'
        }
    ]
    return render_template("index.html",
                            title='Home',
                            user=user,
                            posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s'
                % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])