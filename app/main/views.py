from flask import render_template 
from . import main
from ..requests import get_quotes


@main.route('/')
def index():
    '''
    returns the index page and renders its contents
    '''
    title='Welcome to this blog app'

    quotes=get_quotes()

    # print(random_quotes)

    return render_template('index.html', title=title, quotes=quotes)