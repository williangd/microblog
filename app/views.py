from flask import render_template
from app import app

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
