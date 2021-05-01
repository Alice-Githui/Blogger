from flask import render_template, request, redirect,url_for,abort
from . import main
from ..requests import get_quotes
from flask_login import login_required
from ..models import User, Post
from .forms import UpdateProfile
from .. import db, photos

@main.route('/')
def index():
    '''
    returns the index page and renders its contents
    '''
    title='Welcome to this blog app'

    quotes=get_quotes()

    return render_template('index.html', title=title, quotes=quotes)

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user=user)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    updateform=UpdateProfile()
    if updateform.validate_on_submit():
        user.bio=updateform.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))
    return render_template('profile/update.html', updateform=updateform)

@main.route('/user/<uname>/update/pic' methods=['POST'])
@login_required
def update_pic(uname):
    user=User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.profile_pic_path=path
        db.session.commit()

    return redirect(url_for('main.profile', uname=uname))