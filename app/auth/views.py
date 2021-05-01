from flask import render_template, redirect, url_for, flash,request
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from flask_login import login_user,logout_user,login_required

@auth.route('/login')
def login():
    '''
    renders the login page
    '''
    loginform=LoginForm()
    if loginform.validate_on_submit():
        user=User.query.filter_by(email=loginform.email.data).first()
        if user is not None and user.verify_password(loginform.password.data):
            login_user(user, loginform.remember.data)
            return redirect(request.args.get('next' or url_for('main.index')))

        flash('Invalid Username or Password')

    title='Blogger Login'
    return render_template('auth/login.html', loginform=loginform, title=title)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    regform=RegistrationForm()
    if regform.validate_on_submit():
        user=User(email=regform.email.data, username=regform.username.data, password=regform.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
        title='New Account'
    return render_template('auth/register.html', regform=regform)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
