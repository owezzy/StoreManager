from passlib.hash import pbkdf2_sha256 as sha256

users = []


class User:

    def __init__(self, username, email, password):
        # We will automatically generate the new id
        self.id = len(users) + 1
        self.username = username
        self.email = email
        self.password = password

    def create_new_user(self):
        new_user = {'id': self.id, 'username': self.username, 'email': self.email, 'password': self.password}
        users.append(new_user)
        return new_user

    @staticmethod
    def find_by_username(username):
        return next((user for user in users if user["username"] == username), False)

    @staticmethod
    def find_by_email_address(email):
        return next((user for user in users if user["email"] == email), False)

    @staticmethod
    def generate_password_hash(password):
        return sha256.hash(password)

    def check_hash(password, hash):
        return sha256.verify(password, hash)
