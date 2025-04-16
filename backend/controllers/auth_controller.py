import json
from tornado.web import RequestHandler
from backend.repositories.user_repository import UserRepository
from backend.utils.security import hash_password, generate_jwt
from backend.views.responses import success_response, error_response

class AuthRegisterHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    def options(self):
        self.set_status(204)
        self.finish()

    async def post(self):
        try:
            data = json.loads(self.request.body)
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                self.set_status(400)
                await self.finish(error_response('Username and password are required'))
                return

            try:
                hashed_password = hash_password(password)
                user = UserRepository.create_user(username, hashed_password)
                self.set_status(201)
                await self.finish(success_response({'message': 'User registered successfully', 'user_id': user.id, 'username': user.username}))  # Añade await
            except ValueError as e:
                self.set_status(409)
                await self.finish(error_response(str(e)))
            except Exception as e:
                self.set_status(500)
                await self.finish(error_response(f'Error during registration: {str(e)}'))
        except json.JSONDecodeError:
            self.set_status(400)
            await self.finish(error_response("Invalid JSON"))

class AuthLoginHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    def options(self):
        self.set_status(204)
        self.finish()

    async def post(self):
        try:
            data = json.loads(self.request.body)
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                self.set_status(400)
                await self.finish(error_response('Username and password are required'))
                return

            user = UserRepository.get_user_by_username(username)
            if user and UserRepository.verify_user_password(user, password):
                token = generate_jwt(user.id, user.username, user.role)
                await self.finish(success_response({'token': token}))
            else:
                self.set_status(401)
                await self.finish(error_response('Invalid credentials'))
        except json.JSONDecodeError:
            self.set_status(400)
            await self.finish(error_response("Invalid JSON"))
        except Exception as e:
            self.set_status(500)
            await self.finish(error_response(f'Error during login: {str(e)}'))