import conf
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_marshmallow import Marshmallow


# Flask init
app = Flask(__name__)
app.config['ENV'] = conf.ENV
app.config['SQLALCHEMY_DATABASE_URI'] = conf.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# CORS
cors = CORS(app)

# SQLAlchemy init
db = SQLAlchemy(app)

# Flask RESTful init
api = Api(app)


if __name__ == '__main__':
    # Bind resources
    from resources.user_resource import UserResrouce
    api.add_resource(UserResrouce, '/user/<string:service>')

    # Create User Table
    from models.user_model import db
    db.create_all()

    # Run Flask service
    app.run(
        host=conf.HOST,
        port=conf.PORT,
        debug=False
    )
