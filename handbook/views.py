import os
from flask import Flask
from flask import render_template
from handbook import app

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATE_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))