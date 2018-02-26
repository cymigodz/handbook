#import framework
from flask import Flask
#circular import __init__.py to gain access to app instance
from handbook import app

import pymongo
from pymongo import MongoClient


# Default
# client = MongoClient() 
# By IP Address and Port
client = MongoClient('localhost', 27017)
# By Mongo URI
# client = MongoClient('mongodb://localhost:27017/') 

db = client["db-test"]
collection = db["col-test"]