from datetime import datetime
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

    def post(self):
        user_data = self.middleware.read_post()
        user_obj = User(
            username=user_data['username'],
            email=user_data['email'],
            passphrase=user_data['passphrase'],
            created_at=datetime.now(),
            updated_at=datetime.now())

        # Call QueryService and bind User model as resource
        user_service = ResourceQueryService(db.session, user_obj)
        user_service.create_one(user_obj)
        return {}, 201

    def get(self):
        user_data = self.middleware.read_get()

        # Call QueryService passing "email" arg
        user_service = ResourceQueryService(db.session, User)
        result = user_service.get_by_email(user_data['email'])
        user_dump = self.middleware.schema.dump(result)
        return user_dump, 200

    def put(self):
        user_data = self.middleware.read_update()
        # Call QueryService and bind User model as resource
        user_service = ResourceQueryService(db.session, user_data)
        return {}, 200

    def delete(self):
        pass
