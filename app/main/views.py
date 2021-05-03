from flask import render_template, request, redirect,url_for,abort,flash
from . import main
from ..requests import get_quotes
from flask_login import login_required, current_user
from ..models import User,Post,Comment, Subscriber
from .forms import UpdateProfile,BlogForm,CommentForm, UpdateBlog
from .. import db, photos
import markdown2

@main.route('/')
def index():

    posts=Post.query.all()
    allposts=Post.query.order_by(Post.time.desc()).filter_by(category="allposts")   
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
    subscribers=Subscriber.query.all()
    form=BlogForm()

    if form.validate_on_submit():
        category=form.category.data
        title=form.title.data
        blog=form.blog.data
        user_id=current_user

        new_post=Post(category=category,title=title, blog=blog, user_id=user_id._get_current_object().id)

        db.session.add(new_post)
        db.session.commit()

        for subscriber in subscribers:
            subscriber_message("A new blog has been posted on our site.","email/new_post", subscriber.email, user=user)

        return redirect(url_for('main.index'))

    return render_template('newblog.html', form=form, title='Create New Post', legend='New Post')

@main.route('/comment/<int:post_id>', methods=['GET', 'POST'])
def new_comment(post_id):
    commentform=CommentForm()
    post = Post.query.get(post_id)
    all_comments = Comment.query.filter_by(post_id = post_id).all()

    if commentform.validate_on_submit():
        comment=commentform.comment.data
        post_id=post_id

        new_comment=Comment(comment=comment, post_id=post_id)
        new_comment.save_comment()

        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', post_id=post_id, comment=comment))
    print(all_comments)
    return render_template('comment.html', commentform=commentform, all_comments=all_comments,post=post)


@main.route('/comment/delete/<int:comment_id>', methods=['GET','POST'])
@login_required
def delete_comment(comment_id):

    comments = Comment.query.filter_by(id = comment_id).all()

    for comment in comments:
        db.session.delete(comment)
        db.session.commit()    

    return redirect(url_for('.new_post'))


@main.route('/post/delete/<int:post_id>', methods=['GET','POST'])
@login_required
def delete_post(post_id):

    post=Post.query.filter_by(id = post_id).first()

    if post.users !=current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post=Post.query.get(post_id)

    if post.users !=current_user:
        abort (403)

    form=BlogForm()

    if form.validate_on_submit():
        post.category=form.category.data
        post.title=form.title.data
        post.blog=form.blog.data

        db.session.commit()

        return redirect(url_for('main.index', id=post.id))

    elif request.method=='GET':
        form.category.data=post.category
        form.title.data=post.title
        form.blog.data=post.blog

    return render_template('newblog.html', form=form, post=post, title='Update Post', legend='Update Post')



