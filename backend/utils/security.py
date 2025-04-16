import bcrypt
import jwt
from datetime import datetime, timedelta
from tornado.web import HTTPError

SECRET_KEY = "admin_secret123"

def hash_password(password):
    hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def generate_jwt(user_id, username, role, expires_in_minutes=30):
    payload = {
        'user_id': user_id,
        'username': username,
        'role': role,
        'exp': datetime.utcnow() + timedelta(minutes=expires_in_minutes)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPError(401, reason="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPError(401, reason="Invalid token")

def auth_required(handler_method):
    async def wrapper(self, *args, **kwargs):
        auth_header = self.request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            self.set_status(401)
            self.finish({'error': 'Authentication required'})
            return
        token = auth_header[7:]  # Remove 'Bearer '
        try:
            payload = decode_jwt(token)
            self.current_user = payload
            await handler_method(self, *args, **kwargs)
        except HTTPError as e:
            self.set_status(e.status_code)
            self.finish({'error': e.reason})
        except Exception as e:
            self.set_status(500)
            self.finish({'error': 'Internal server error'})
    return wrapper

def admin_required(handler_method):
    @auth_required
    async def wrapper(self, *args, **kwargs):
        if getattr(self, 'current_user', {}).get('role') == 'admin':
            await handler_method(self, *args, **kwargs)
        else:
            self.set_status(403)
            self.finish({'error': 'Admin privileges required'})
    return wrapper