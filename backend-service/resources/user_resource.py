from hashlib import md5
from datetime import datetime
from flask import jsonify, abort
from flask_restful import Resource
from app import db
from services.user_middleware import UserMiddleware, UserSchema
from services.user_service import ResourceQueryService
from models.user_model import User


class UserResrouce(Resource):
    """
    User API
    """
    middleware = UserMiddleware()
    def post(self, service):
        if service == 'signUp':
            return self.user_signup_service()
        elif service == 'signIn':
            return self.user_signin_service()

    def user_signup_service(self):
        user_data = self.middleware.read_post()
        user_obj = User(
            username=user_data['username'],
            email=user_data['email'],
            passphrase=md5(
                # encrypt user passphrase
                user_data['passphrase']\
                .encode('utf-8')).hexdigest(),
            created_at=datetime.now(),
            updated_at=datetime.now())

        # Call QueryService and bind User model as resource
        user_service = ResourceQueryService(db.session, user_obj)
        result_data = user_service.create_one(user_obj)
        if not result_data:
            return {}, 201
        else:
            return abort(400, result_data)

    def user_signin_service(self):
        user_data = self.middleware.read_get()

        # Call QueryService passing "email" arg
        user_service = ResourceQueryService(db.session, User)
        result = user_service.get_by_email(user_data['email'])

        user_data['passphrase'] = md5(user_data['passphrase'].encode('utf-8'))
        if result and user_data['passphrase'].hexdigest() == result.passphrase:
            # Serialize object
            user_dump = self.middleware.schema.dump(result)
            return user_dump, 200
        else:
            return abort(401, 'authentication error')

    def put(self):
        user_data = self.middleware.read_update()
        # Call QueryService and bind User model as resource
        # user_service = ResourceQueryService(db.session, user_data)
        return {}, 200

    def delete(self):
        pass
