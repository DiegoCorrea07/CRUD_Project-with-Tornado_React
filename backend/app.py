import tornado.ioloop
from backend.db.db_config import get_connection
from views.routes import make_app

if __name__ == "__main__":
    try:
        # Verifica y crea la tabla si no existe
        connection = get_connection()
        connection.close()
        print("Tabla 'flights' verificada/creada correctamente.") # Para depuración
    except Exception as e:
        print(f"Error al verificar/crear la tabla: {e}") # Para depuración

    app = make_app()  # Utiliza la función importada para crear la aplicación
    app.listen(8888)
    print("Server started at http://localhost:8888") # URL de inicio del servidor
    tornado.ioloop.IOLoop.current().start()
