from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quotes:
    '''
    quotes class to define the quotes objects
    '''
    def __init__(self, id, author, quote,permalink):
        self.id = id
        self.author=author
        self.quote=quote
        self.permalink=permalink

class User(UserMixin,db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255), index=True)
    bio=db.Column(db.String)
    email=db.Column(db.String,unique=True,index=True)
    profile_pic_path=db.Column(db.String)
    pass_secure=db.Column(db.String(200))
    blogposts=db.relationship('Post', foreign_keys='Post.user_id',backref="users", lazy="dynamic")
    comment=db.relationship('Comment', foreign_keys="Comment.user_id", backref="users", lazy="dynamic")
    like=db.relationship('Like', foreign_keys="Like.user_id", backref="users", lazy="dynamic")
    dislike=db.relationship('Dislike', foreign_keys="Dislike.user_id", backref="users", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User{self.username}'

class Post(db.Model):
    __tablename__='posts'

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String)
    blog=db.Column(db.Text)
    category=db.Column(db.String)
    time=db.Column(db.DateTime(),default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    comments=db.relationship('Comment', foreign_keys="Comment.post_id",backref='post', lazy="dynamic")
    like=db.relationship('Like', foreign_keys="Like.post_id", backref="posts", lazy="dynamic")
    dislike=db.relationship('Dislike', foreign_keys="Dislike.post_id", backref="posts", lazy="dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls,id):
        posts=Post.query.filter_by(post_id=id).all()
        return posts

    def __repr__(self):
        return f'Post{self.title}'

class Category(db.Model):
    __tablename__='category'

    id=db.Column(db.Integer, primary_key=True)
    category=db.Column(db.String)

    def __repr__(self):
        return f'Category{self.category}'

class Comment(db.Model):
    __tablename__='comments'

    id=db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.String)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id=db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,post_id):
        comments=Comment.query.filter_by(post_id=post_id).all()
        return comments

    def __repr__(self):
        return f'Comment{self.comment}'

class Subscriber(db.Model):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'

class Like(db.Model):
    __tablename__='like'

    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id=db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save_like(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        likes=Like.query.filter_by(post_id=id).all()
        return likes


    def __repr__(self):
        return f'Like{self.user_id}'

class Dislike(db.Model):
    __tablename__='dislike'

    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id=db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save_dislikes(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_dislikes(cls,id):
        dislikes=Dislike.query.filter_by(post_id=id).all()
        return dislikes


    def __repr__(self):
        return f'Dislike{self.user_id}'



    

