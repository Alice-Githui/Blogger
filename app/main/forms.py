from flask_wtf import FlaskForm 
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tell us something about yourself', validators=[Required()])
    submit=SubmitField('Submit')

class BlogForm(FlaskForm):
    category=SelectField('Select Category', choices=[('allposts', 'All Blog Posts')])
    title=StringField('Blog Title:', validators=[Required()])
    blog=StringField('Body:', validators=[Required()])
    submit=SubmitField('Post')

class UpdateBlog(FlaskForm):
    category=SelectField('Select Category', choices=[('allposts', 'All Blog Posts')])
    title=StringField('Blog Title:', validators=[Required()])
    blog=StringField('Body:', validators=[Required()])
    submit=SubmitField('Post')

class CommentForm(FlaskForm):
    comment=TextAreaField('Add Comment', validators=[Required()])
    submit=SubmitField('Submit')