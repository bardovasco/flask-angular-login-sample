"""
Settings for the Flask app backend
service.
"""
import os


basedir = os.path.abspath(os.path.dirname(__file__))

### App-related config
HOST=''
PORT=5000
ENV='develop'

### DB-related config
ENGINE='sqlite:////'
ADDRESS=basedir
DATABASE='user.db'
DATABASE_URI = '{}{}/{}'.format(ENGINE, ADDRESS, DATABASE)
