from flask import render_template, request, redirect,url_for,abort
from . import main
from ..requests import get_quotes
from flask_login import login_required, current_user
from ..models import User,Post
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db, photos

@main.route('/')
def index():
    posts=Post.query.all()
    allposts=Post.query.filter_by(category="allposts")   
    title='Welcome to this blog app'

    quotes=get_quotes()

    return render_template('index.html', title=title, quotes=quotes, posts=posts, allposts=allposts)

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

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user=User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.profile_pic_path=path
        db.session.commit()

    return redirect(url_for('main.profile', uname=uname))

@main.route('/newpost', methods=['GET', 'POST'])
@login_required
def new_post():
    form=BlogForm()

    if form.validate_on_submit():
        category=form.category.data
        title=form.title.data
        blog=form.blog.data
        user_id=current_user

        new_post=Post(category=category,title=title, blog=blog, user_id=user_id._get_current_object().id)

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('newblog.html', form=form)

