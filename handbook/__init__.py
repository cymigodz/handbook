# import framework
from flask import Flask
# reference to the instance of application itself
# "__name__" is a special variable that gets the app name
# "__name__" is ecessary because script is named as "__main__" while executing
app = Flask(__name__)
# Auto reload when html change is detected
app.jinja_env.auto_reload = True
# Auto reload when html change is detected
app.config['TEMPLATE_AUTO_RELOAD'] = True 

# importing modules/packages that forms the application
import handbook.models # database models
import handbook.views # routing and page view generations
