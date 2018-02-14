# required for mapping dev server to public on c9 platfoorm
import os
# import framework
from flask import Flask
# reference to the instance of application itself
# "__name__" is a special variable that gets the app name
# "__name__" is ecessary because script is named as "__main__" while executing
app = Flask(__name__)

# importing modules/packages that forms the application
import handbook.models # database models
import handbook.views # routing and page view generations


# Auto reload when html change is detected
app.jinja_env.auto_reload = True
# Auto reload when html change is detected
app.config['TEMPLATE_AUTO_RELOAD'] = True 
# Map the server to public, method is instructed by c9 platform.
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))