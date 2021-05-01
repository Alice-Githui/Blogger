from flask_wtf import FlaskForm 
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tell us something about yourself', validators=[Required()])
    submit=SubmitField('Submit')