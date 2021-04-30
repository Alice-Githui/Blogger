from flask import render_template 
from . import main

@main.route('/')
def index():
    '''
    returns the index page and renders its contents
    '''
    return render_template('index.html')