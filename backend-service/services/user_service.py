from datetime import datetime
from app import db
from sqlalchemy.exc import (
    DBAPIError,
    IntegrityError,
    InterfaceError
)


class DBService:
    @staticmethod
    def db_query_callback(db_sess, query_callback):
        """
        Interface function that receives
        a resource query and a database
        session to commit query, and it
        returns the database output (if
        it is the case).
        """
        try:
            result = query_callback()
            db_sess.commit()
        except (DBAPIError,IntegrityError,InterfaceError) as e:
            print('database error', e)
            db_sess.rollback()
        finally:
            if result:
                return result

class ResourceQueryService(DBService):
    def __init__(self, db_session, resource):
        # DBService.__init__()
        self.db_service = DBService()
        self.db_session = db_session
        self.resource = resource

    def create_one(self, data) -> None:
        result = None
        try:
            self.db_session.add(data)
            self.db_session.commit()
        except (DBAPIError,IntegrityError,InterfaceError) as e:
            result = str(e.orig)
            self.db_session.rollback()
        finally:
            return result

    def get_by_email(self, filter_detail) -> 'User':
        """
        id: integer
        """
        query_cb = (lambda: self.resource.query.filter_by(email=filter_detail).first())
        return self.db_service.db_query_callback(self.db_session, query_cb)


    def update_one(self, data):
        """
        Example input;
        data = {
            'id':
            'newEmail':
            'newUsername':
            'newPassPhrase'
        }
        """
        # Base query
        query = self.resource.query.filter_by(id=data['id'])
        # Extend query
        if data.get('new_user_name'):
            query.update({'username': data['new_user_name']})
        if data.get('new_email'):
            query.update({'email': data['new_email']})
        if data.get('new_passphrase'):
            query.update({'passphrase': data['new_passphrase']})
        query.update({'updated_at': datetime.now()})

        # Query lambda calback
        query_cb = (lambda: query)
        return self.db_query_callback(self.db_session, query_cb)

    def delete_one(self, id):
        # Query lambda calback
        query_cb = (lambda: self.resource.query.filter_by(id=id).delete())
        return self.db_query_callback(self.db_session, query_cb)

