#import framework
from flask import Flask
#circular import __init__.py to gain access to app instance
from handbook import app

import pymongo
from pymongo import MongoClient

import datetime


# Default
# client = MongoClient() 
# By IP Address and Port
client = MongoClient('localhost', 27017)
# By Mongo URI
# client = MongoClient('mongodb://localhost:27017/') 

runTest = False
if runTest:
    print("models.py test code is running")
    db = client["blog"]
    collection = db["posts"]
    testpost = collection.find_one()
    print(testpost)
else:
    print("models.py test code is not running")


class Blog:
    @staticmethod
    def TEST_getPost():
        db = client["blog"]
        collection = db["posts"]
        testpost = collection.find_one()
        return testpost