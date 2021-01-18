"""
Explaination of dual data parser:
    - RequestParser: Data validation
    at HTTP-level.
    - Marshmallow: Data parse to keep
    snakecase format with Model objects.
"""
from flask_restful.reqparse import RequestParser
from marshmallow import Schema, fields, post_dump



class UserSchema(Schema):
    """
    User Schema to dump and load
    our user objects.
    """
    # Default fields
    id = fields.Integer(attribute='id')
    username = fields.String(attribute='username')
    email = fields.String(attribute='email')
    passPhrase = fields.String(attribute='passphrase', load_only=True)
    createdAt = fields.String(attribute='created_at')
    updatedAt = fields.String(attribute='updated_at')
    # Fields for PUT method
    newEmail = fields.String(attribute='new_email', load_only=True)
    newUsername = fields.String(attribute='new_username', load_only=True)
    newPassPhrase = fields.String(attribute='new_passphrase', load_only=True)

    @post_dump
    def delete_null_values(self, data, *args, **kwargs):
        """
        PreDump function to clear
        unnecessary fields.
        """
        for k,v in data.items():
            if not v:
                del data[k]
        return data

class UserMiddleware(RequestParser):
    """
    Middleware module that handles
    validation of request arguments.
    """
    schema = UserSchema()
    def __init__(self):
        RequestParser.__init__(self)

    def read_post(self):
        self.clear_args()

        # Parse args
        self.add_argument('username', type=str, location=('json'), required=True, case_sensitive=True)
        self.add_argument('email', type=str, location=('json'), required=True, case_sensitive=True)
        self.add_argument('passPhrase', type=str, location=('json'), required=True, case_sensitive=True)

        # Read args
        data = self.parse_args(strict=True)
        # Clear current args
        self.clear_args()

        # Schema load
        loaded_data = self.schema.load(data)
        return loaded_data

    def read_get(self):
        self.clear_args()

        # Parse args
        self.add_argument('email', type=str, location=('json'), required=True, case_sensitive=True)
        self.add_argument('passPhrase', type=str, location=('json'), required=True, case_sensitive=True)

        # Read args
        data = self.parse_args(strict=True)
        # Clear current args
        self.clear_args()

        # Schema load
        loaded_data = self.schema.load(data)
        return loaded_data

    def read_update(self):
        self.clear_args()

        # Parse args
        self.add_argument('id', type=int, location=('json'), required=True)
        self.add_argument('newEmail', type=str, location=('json'), required=False)
        self.add_argument('newUsername', type=str, location=('json'), required=False)
        self.add_argument('newPassPhrase', type=str, location=('json'), required=False)
        # Read args
        data = self.parse_args(strict=True)
        # Clear current args
        self.clear_args()

        # Schema load
        loaded_data = self.schema.load(data)
        return loaded_data

    def clear_args(self) -> None:
        for arg in self.args:
            self.remove_argument(arg.name)

