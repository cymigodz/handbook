#import framework
from flask import Flask
#circular import __init__.py to gain access to app instance
from handbook import app
#used to render html templates in routings
from flask import render_template

#Route - Landing page
@app.route('/')
def index():
    return render_template('index.html')

