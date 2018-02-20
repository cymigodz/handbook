#import framework
from flask import Flask
#circular import __init__.py to gain access to app instance
from handbook import app

import pymongo
