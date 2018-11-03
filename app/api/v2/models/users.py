from passlib.hash import pbkdf2_sha256 as sha256
from psycopg2 import Error

from app.db import cur


class User:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.role = 0

    def create_new_user(self):
        try:
            cur.execute(
                """INSERT INTO users (username, email, password)
                   VALUES ('%s','%s','%s')""",
                (self.username, self.email, self.password))
            cur.commit()
            return 'new_user registered successfully'
        except Exception as er:
            print(er)
            return 'Registration Failed'

    # checks if user with the id exists
    @staticmethod
    def find_by_id(user_id):

        cur.execute("""SELECT * FROM users WHERE id='{}' """.format(user_id))
        rows = cur.fetchone()
        if rows:
            return True
        return False

    @staticmethod
    def find_by_username(username):
        cur.execute("""SELECT * FROM users WHERE username='{}' """.format(username))
        rows = cur.fetchone()
        return rows

    @staticmethod
    def find_by_email(email):
        cur.execute("""SELECT * FROM users WHERE email='{}' """.format(email))
        rows = cur.fetchone()
        return rows

    # checks if user is admin
    @staticmethod
    def is_admin(username):

        cur.execute("""SELECT * FROM users WHERE username='{}' """.format(username))
        rows = cur.fetchone()
        if rows:
            if rows["role"] == 1:
                return True
            return False
        return False

    @staticmethod
    def make_admin(username):
        role = 1
        try:
            cur.execute("""UPDATE users  SET role='{}'  WHERE id='{}' """.format(role, username))
            cur.commit()
            return 'Store attendant authorized as Admin'
        except (Exception, Error) as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    @staticmethod
    def generate_password_hash(password):
        return sha256.hash(password)

    def check_hash(password, hash):
        return sha256.verify(password, hash)
