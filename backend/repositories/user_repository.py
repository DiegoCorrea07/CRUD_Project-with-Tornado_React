import pyodbc
from backend.models.user import User
from backend.db.db_config import get_connection
from backend.utils.security import verify_password

class UserRepository:
    @staticmethod
    def create_user(username, password_hash, role='user'):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                sql = """
                INSERT INTO users (username, password_hash, role)
                VALUES (?, ?, ?)
                """
                cursor.execute(sql, username, password_hash, role)
                conn.commit()
                # Obtener el ID del usuario recién insertado
                cursor.execute("SELECT SCOPE_IDENTITY()")
                user_id = cursor.fetchone()[0]
                return User(id=user_id, username=username, password_hash=password_hash, role=role)
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '23000':  # Código de error para violación de restricción única (username)
                raise ValueError("Username already exists")
            else:
                raise

    @staticmethod
    def get_user_by_username(username):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                sql = "SELECT id, username, password_hash, role FROM users WHERE username = ?"
                cursor.execute(sql, username)
                row = cursor.fetchone()
                if row:
                    return User(id=row[0], username=row[1], password_hash=row[2], role=row[3])
                return None
        except pyodbc.Error as ex:
            print(f"Error getting user by username: {ex}")
            return None

    @staticmethod
    def get_user_by_id(user_id):
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                sql = "SELECT id, username, password_hash, role FROM users WHERE id = ?"
                cursor.execute(sql, user_id)
                row = cursor.fetchone()
                if row:
                    return User(id=row[0], username=row[1], password_hash=row[2], role=row[3])
                return None
        except pyodbc.Error as ex:
            print(f"Error getting user by id: {ex}")
            return None

    @staticmethod
    def verify_user_password(user: User, password):
        return verify_password(password, user.password_hash)