#!/bin/sh
cd /home/ubuntu/workspace
# Flask APP
export FLASK_APP=handbook
# Debug mode
# export FLASK_DEBUG=true
#======================


sudo pip install -e .
# python /home/ubuntu/workspace/handbook/__init__.py
python -m flask run
# python -m flask run --host=0.0.0.0 --port=8080
