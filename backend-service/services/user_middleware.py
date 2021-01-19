"""
Explaination of dual data parser:
    - RequestParser: Data validation
    at HTTP-level.
    - Marshmallow: Data parse to keep
    snakecase format with Model objects.
"""
from flask_restful.reqparse import RequestParser
from marshmallow import Schema, fields, post_dump, post_load


class UserSchema(Schema):
    """
    Schema to load and dump
    user objects.
    """
    id = fields.Integer(attribute='id')
    username = fields.String(attribute='username')
    email = fields.String(attribute='email')
    createdAt = fields.String(attribute='created_at')
    updatedAt = fields.String(attribute='updated_at')
    passPhrase = fields.String(attribute='passphrase', load_only=True)

class UserMiddleware(RequestParser):
    """
    Middleware module that handles
    validation of request arguments.
    """
    schema = UserSchema()
    def __init__(self):
        RequestParser.__init__(self)

    def read_post(self):
        # Parse args
        self.add_argument('username', type=str, location=('json'), required=True, case_sensitive=True)
        self.add_argument('email', type=str, location=('json'), required=True, case_sensitive=True)
        self.add_argument('passPhrase', type=str, location=('json'), required=True, case_sensitive=True)

        # Read args
        data = self.parse_args(strict=True)
        self.remove_argument('username')
        # Schema load
        loaded_data = self.schema.load(data)
        return loaded_data

    def read_get(self):
        # Parse args
        self.add_argument('email', type=str, location=('json'), required=True, case_sensitive=True)
        self.add_argument('passPhrase', type=str, location=('json'), required=True, case_sensitive=True)

        # Read args
        data = self.parse_args(strict=True)
        # Schema load
        loaded_data = self.schema.load(data)
        return loaded_data

