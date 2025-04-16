# Gestión de Vuelos

Un sistema CRUD para la gestión de vuelos, desarrollado con **Python** (Tornado) en el backend y **React** en el frontend, que incluye **autenticación de usuarios (login y registro) y control de permisos** para las operaciones CRUD.

---

## Descripción del Proyecto

Este proyecto permite a los usuarios gestionar vuelos mediante una interfaz web. Además de las funcionalidades CRUD básicas, se han implementado las siguientes características de seguridad y gestión de usuarios:

- **Autenticación de Usuarios:** Los usuarios pueden registrarse e iniciar sesión de forma segura.
- **Control de Permisos:** Las operaciones CRUD están protegidas y requieren privilegios de administrador para ser realizadas (crear, editar, eliminar). Los usuarios regulares solo pueden listar los vuelos y crear nuevos vuelos.
- Editar vuelos existentes (requiere permisos de administrador).
- Eliminar vuelos (requiere permisos de administrador).
- Listar vuelos con detalles como aerolínea, número de vuelo, origen, destino, hora de salida y llegada (accesible para todos los usuarios autenticados).
- Cierre de sesión seguro.

El backend está construido con **Tornado** y utiliza una base de datos SQLServer para almacenar los datos de los vuelos y la información de los usuarios. El frontend está desarrollado con **React** con **Vite** y utiliza `fetch` para interactuar con la API del backend, incluyendo el manejo de tokens JWT para la autenticación y autorización.

---

## Tabla de Contenidos

1. [Instalación](#instalación)
2. [Uso del Proyecto](#uso-del-proyecto)
3. [Control de Permisos](#control-de-permisos)
4. [Características](#características)
5. [Contribución](#contribución)
6. [Créditos](#créditos)
7. [Licencia](#licencia)

---

## Instalación

### Requisitos previos

- **Node.js** y **npm** instalados para el frontend.
- **Python 3.8+** instalado para el backend.
- **pyodbc** (Versión utilizada: 5.2.0)
- **pytz** (Versión utilizada: 2025.2)
- **tornado** (Versión utilizada: 6.4.2)
- **PyJWT** - Para la generación y verificación de tokens JWT en el backend.
- **bcrypt** - Para el hashing seguro de contraseñas en el backend.

### Configuración de la Base de Datos (SQLServer)

1. Asegúrate de tener un servidor SQLServer en funcionamiento.
2. Crea una base de datos llamada `FlightDB` (el nombre que se utiliza en el backend, en el archivo **db_config.py**).
3. Configura el servidor y el driver para la conexión a la base de datos, en el archivo **db_config.py** del backend.
4. **Esquema de la tabla de usuarios:** Asegúrate de tener una tabla `users` con las columnas `id` (INT PRIMARY KEY IDENTITY), `username` (VARCHAR(255) UNIQUE NOT NULL), `password_hash` (VARCHAR(255) NOT NULL), y `role` (VARCHAR(50) NOT NULL DEFAULT 'user').

### Pasos para instalar y ejecutar el proyecto

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/DiegoCorrea07/CRUD_Project-with-Tornado_React.git](https://github.com/DiegoCorrea07/CRUD_Project-with-Tornado_React.git)
   
```markdown
## Configura el Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

El servidor del backend estará disponible en [http://localhost:8888](http://localhost:8888).

---

## Configura el Frontend

```bash
cd ../frontend
npm install
npm run dev
```

El servidor del frontend estará disponible en [http://localhost:5173](http://localhost:5173).

---

## Uso del Proyecto

1. Accede a la interfaz web en [http://localhost:5173](http://localhost:5173).
2. Los usuarios nuevos deben registrarse haciendo clic en el enlace **Regístrate** e ingresando un Usuario y Contraseña.
3. Los usuarios registrados pueden iniciar sesión con su Usuario y Contraseña.
4. Una vez autenticado, se mostrará la lista de vuelos.
5. El token JWT se guarda en el almacenamiento local del navegador y se incluye en las cabeceras de las peticiones al backend para la autenticación y autorización.
6. El botón **Eliminar**, solo estarán habilitados para los usuarios con el rol de administrador.
7. Los usuarios pueden cerrar sesión utilizando el botón **Cerrar Sesión**, lo que elimina el token del almacenamiento local y los redirige a la página de inicio de sesión.

---

## Control de Permisos

El sistema implementa un control de permisos basado en roles, utilizando la información del rol contenida en el token JWT:

- **Administradores (role: 'admin')**: Tienen permiso para realizar todas las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los vuelos. El backend verifica el token y el rol antes de permitir estas operaciones.
- **Usuarios Regulares (role: 'user')**: Solo tienen permiso para leer (listar) los vuelos y para crear.

El backend verifica el token JWT enviado por el frontend en cada petición protegida para determinar el rol del usuario y permitir o denegar la operación, devolviendo un error **403 (Forbidden)** si un usuario sin los permisos adecuados intenta realizar una acción restringida.

---

## Características

- **Autenticación Segura**: Registro e inicio de sesión de usuarios con almacenamiento seguro de contraseñas utilizando hashing con bcrypt.
- **Autorización Basada en Roles**: Control de acceso a las operaciones CRUD basado en el rol del usuario (administrador o usuario regular), gestionado mediante tokens JWT.
- **Tokens JWT**: Utilización de JSON Web Tokens (PyJWT en el backend) para la autenticación y autorización de las peticiones al backend. El token contiene información sobre el usuario y su rol.
- **Validaciones Robustas**:
  - Evita la creación de vuelos duplicados.
  - Verifica que se ingresen datos en todos los campos.
- **Interfaz Amigable**:
  - Diseño limpio y funcional con React.
- **API RESTful**:
  - Endpoints para operaciones CRUD (GET, POST, PUT, DELETE).
  - Endpoints para registro (`POST /api/register`) e inicio de sesión (`POST /api/login`).
- **CORS Habilitado**:
  - Permite la comunicación entre el frontend y el backend.

---

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Haz un push a la rama:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Abre un Pull Request.

---

## Créditos

Este proyecto fue desarrollado por:

- **Diego Correa**
- [GitHub](https://github.com/DiegoCorrea07)

---

## Licencia

Este proyecto está licenciado bajo la **MIT License**. Puedes usar, modificar y distribuir este proyecto libremente.

¡Gracias por revisar este proyecto! 😊
```