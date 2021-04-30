from . import db
from datetime import datetime

class Quotes:
    '''
    quotes class to define the quotes objects
    '''
    def __init__(self, id, author, quote,permalink):
        self.id = id
        self.author=author
        self.quote=quote
        self.permalink=permalink

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    bio=db.Column(db.String)
    email=db.Column(db.String)
    profile_pic=db.Column(db.String)
    pass_secure=db.Column(db.String(200))
    blogposts=db.relationship('Post', foreign_keys='Post.user_id',backref="users", lazy="dynamic")
    comment=db.relationship('Comment', foreign_keys="Comment.user_id", backref="users", lazy="dynamic")
    like=db.relationship('Like', foreign_keys="Like.user_id", backref="users", lazy="dynamic")
    dislike=db.relationship('Dislike', foreign_keys="Dislike.user_id", backref="users", lazy="dynamic")

    def __repr__(self):
        return f'User{self.username}'

class Post(db.Model):
    __tablename__='posts'

    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String)
    blog=db.Column(db.Text)
    time=db.Column(db.DateTime(),default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id=db.Column(db.Integer, db.ForeignKey('category.id'))
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
    post = db.relationship('Post', foreign_keys='Post.category_id', backref='category', lazy="dynamic")

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

    @classmethod
    def get_comment(cls,post_id):
        comments=Comment.query.filter_by(post_id=post_id).all()
        return comments

    def __repr__(self):
        return f'Comment{self.comment}'

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

    

