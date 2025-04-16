import tornado.web
from backend.controllers.flight_controller import FlightController
from backend.controllers.auth_controller import AuthRegisterHandler, AuthLoginHandler
from backend.utils.security import auth_required, admin_required

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Welcome to the Flight CRUD API")

class FlightHandler(tornado.web.RequestHandler):
    controller = FlightController()

    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type, Authorization")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE")

    def options(self, flight_id=None):
        self.set_status(204)
        self.finish()

    @auth_required
    async def get(self, flight_id=None):
        if flight_id:
            self.write(self.controller.get_by_id(flight_id))
        else:
            self.write(self.controller.get_all())

    @auth_required
    async def post(self):
        """Crear un nuevo vuelo."""
        flight_data = tornado.escape.json_decode(self.request.body)
        self.write(self.controller.create(flight_data))

    @admin_required
    async def put(self, flight_id):
        """Actualizar un vuelo existente (solo para admins)."""
        flight_data = tornado.escape.json_decode(self.request.body)
        self.write(self.controller.update(flight_id, flight_data))

    @admin_required
    async def delete(self, flight_id):
        """Eliminar un vuelo (solo para admins)."""
        self.write(self.controller.delete(flight_id))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/register", AuthRegisterHandler),
        (r"/api/login", AuthLoginHandler),
        (r"/api/flights", FlightHandler),  # Para operaciones con todos los vuelos
        (r"/api/flights/([0-9]+)", FlightHandler),  # Para operaciones con un vuelo específico
    ])