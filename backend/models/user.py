
class User:
    def __init__(self, username, password_hash, role='user', id=None):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.role = role

    def __repr__(self):
        return f"<User(username='{self.username}', role='{self.role}')>"