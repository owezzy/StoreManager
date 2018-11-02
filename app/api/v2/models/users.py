import psycopg2

from passlib.hash import pbkdf2_sha256 as sha256
from psycopg2 import sql, extras, Error


from app.db import connect

# users = []
curr = connect.cursor(cursor_factory=extras.RealDictConnection)


class User:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.role = 0

    def create_new_user(self):
        try:
            curr.execute(
                """INSERT INTO users (username, email, password)
                   VALUES ('%s','%s','%s')""",
                (self.username, self.email, self.password))
            connect.commit()
            return 'new_user registered successfully'
        except Exception as er:
            print(er)
            return 'Registration Failed'

    # checks if user with the id exists
    @staticmethod
    def find_by_id(user_id):

        curr.execute("""SELECT * FROM users WHERE id='{}' """.format(user_id))
        rows = curr.fetchone()
        if rows:
            return True
        return False

    @staticmethod
    def find_by_username(username):
        curr.execute("""SELECT * FROM users WHERE username='{}' """.format(username))
        rows = curr.fetchone()
        return rows

    @staticmethod
    def find_by_email_address(email):
        curr.execute("""SELECT * FROM users WHERE email='{}' """.format(email))
        rows = curr.fetchone()
        return rows

    # checks if user is admin
    @staticmethod
    def is_admin(username):

        curr.execute("""SELECT * FROM users WHERE username='{}' """.format(username))
        rows = curr.fetchone()
        if rows:
            if rows["role"] == 1:
                return True
            return False
        return False

    @staticmethod
    def make_admin(username):
        role = 1
        try:
            curr.execute("""UPDATE users  SET role='{}'  WHERE id='{}' """.format(role, username))
            connect.commit()
            return 'Store attendant authorized as Admin'
        except (Exception, psycopg2.Error) as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    @staticmethod
    def generate_password_hash(password):
        return sha256.hash(password)

    def check_hash(password, hash):
        return sha256.verify(password, hash)

    connect.commit()
