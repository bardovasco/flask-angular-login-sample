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

# SQLAlchemy init
db = SQLAlchemy(app)

# Flask RESTful init
api = Api(app)

# Home route redirect to /user
@app.route('/', methods=['GET'])
def home_redirect():
    return redirect('http://127.0.0.1/user')

# @app.before_request
# def db_setup() -> None:
    # from models.user_model import db
    # # Create User Table
    # db.create_all()


if __name__ == '__main__':
    # Bind resources
    from resources.user_resource import UserResrouce
    api.add_resource(UserResrouce, '/user')

    # Create User Table
    from models.user_model import db
    db.create_all()

    # Run Flask service
    app.run(
        host=conf.HOST,
        port=conf.PORT,
        debug=False
    )
