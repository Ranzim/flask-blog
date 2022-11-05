from flask import Flask , render_template, flash, url_for, redirect

from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm

post = [
    { 
        'author': 'Prabin', 
        'title': 'Blog1',
        'content': 'First Post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Ravi',
        'title': 'Blog2',
        'content': 'Second Post content',
        'date_posted': 'April 20, 2020'
    }
]


@app.route("/")
def home(): 
    return render_template('home.html', posts=post)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('Logged IN', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed', 'danger')

    return render_template('login.html', title='Login', form = form)

@app.route("/one")
@app.route("/two")
def two_route():
    return "two Route Handing same function!"