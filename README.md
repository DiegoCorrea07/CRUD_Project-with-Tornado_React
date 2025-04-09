# Gestión de Vuelos

Un sistema CRUD para la gestión de vuelos, desarrollado con **Python** (Tornado) en el backend y **React** en el frontend.

---

## Descripción del Proyecto

Este proyecto permite a los usuarios gestionar vuelos mediante una interfaz web. Las funcionalidades principales incluyen:

- Crear nuevos vuelos.
- Editar vuelos existentes.
- Eliminar vuelos.
- Listar vuelos con detalles como aerolínea, número de vuelo, origen, destino, hora de salida y llegada.

El backend está construido con **Tornado** y utiliza una base de datos SQLServer para almacenar los datos de los vuelos. El frontend está desarrollado con **React** con **Vite** y utiliza `fetch` para interactuar con la API del backend.

---

## Tabla de Contenidos

1. [Instalación](#instalación)  
2. [Uso del Proyecto](#uso-del-proyecto)  
3. [Características](#características)  
4. [Contribución](#contribución)  
5. [Créditos](#créditos)  
6. [Licencia](#licencia)  

---

## Instalación

### Requisitos previos

- **Node.js** y **npm** instalados para el frontend.
- **Python 3.8+** instalado para el backend.
- **pyodbc** (Versión utilizada: 5.2.0)  
- **pytz** (Versión utilizada: 2025.2)
- **tornado** (Versión utilizada: 6.4.2) 

### Configuración de la Base de Datos (SQLServer)

1. Asegúrate de tener un servidor SQLServer en funcionamiento.
2. Crea una base de datos llamada `FlightDB` (el nombre que se utiliza en el backend, en el archivo **db_config.py**).
3. Configura el servidor y el driver para la conexión a la base de datos, en el archivo **db_config.py** del backend.

### Pasos para instalar y ejecutar el proyecto

1. Clona este repositorio:
   ```bash
   git clone https://github.com/DiegoCorrea07/CRUD_Project-with-Tornado_React.git
   ```

2. Configura el backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```
   El servidor del backend estará disponible en `http://localhost:8888`.

3. Configura el frontend:
   ```bash
   cd ../frontend
   npm install
   npm run dev
   ```
   El servidor del frontend estará disponible en `http://localhost:5173`.

---

## Uso del Proyecto

1. Accede a la interfaz web en `http://localhost:5173`.
2. Usa el botón **Nuevo** para agregar un vuelo.
3. Edita o elimina vuelos existentes desde la lista.
4. Los datos se sincronizan automáticamente con el backend.

---

## Características

- **Validaciones robustas**:
  - Evita la creación de vuelos duplicados.
  - Verifica que se ingresen datos en todos los campos.
- **Interfaz amigable**:
  - Diseño limpio y funcional con React.
- **API RESTful**:
  - Endpoints para operaciones CRUD (`GET`, `POST`, `PUT`, `DELETE`).
- **CORS habilitado**:
  - Permite la comunicación entre el frontend y el backend.

---

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz un commit (`git commit -m "Agrega nueva funcionalidad"`).
4. Haz un push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

---

## Créditos

Este proyecto fue desarrollado por:

- **Diego Correa**  
  - [GitHub](https://github.com/DiegoCorrea07)  
  - [LinkedIn](https://www.linkedin.com/in/diego-correa)

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](https://choosealicense.com/licenses/mit/). Puedes usar, modificar y distribuir este proyecto libremente.

--- 

¡Gracias por revisar este proyecto! 😊
