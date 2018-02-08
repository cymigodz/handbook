from flask import Flask
app = Flask(__name__)

import handbook.models
import handbook.views
