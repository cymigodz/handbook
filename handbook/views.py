#import framework
from flask import Flask
#used to render html templates in routings
from flask import render_template
#circular import __init__.py to gain access to variable app
from handbook import app

#Route - Landing page
@app.route('/')
def index():
    return render_template('index.html')

