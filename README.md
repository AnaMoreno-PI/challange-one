# FastAPI Project - Challenge Etapa 6

Este proyecto es una API desarrollada con FastAPI que incluye rutas para gestionar personajes y elementos. Utiliza SQLAlchemy para la interacción con la base de datos y Pydantic para la validación de datos.

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes componentes:

- Python 3.11 o superior
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- Un servidor de base de datos SQL Server

## Configuración del entorno

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en el archivo `.env`:
   ```plaintext
   DB_NAME=
   DB_UID=
   DB_PASS=
   DB_PORT=
   DB_SERVER=
   ENVIRONMENT=
   ```

## Ejecución del proyecto

Inicia el servidor de desarrollo:

```bash
uvicorn main:app --reload
```

Accede a la documentación interactiva de la API en tu navegador:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Estructura del proyecto

```
app/
├── api/
│   ├── models/
│   │   └── characters.py
│   ├── routers/
│   │   ├── characters_router.py
│   │   └── item_router.py
│   └── router.py
├── config/
│   ├── db_config.py
│   └── init_db.py
├── schemas/
│   └── item_schemas.py
├── services/
│   ├── character_services.py
│   └── item_service.py
├── main.py
└── .env
```

## CI/CD Pipeline

Este proyecto utiliza GitHub Actions para implementar un flujo de trabajo de CI/CD que automatiza las pruebas y el despliegue en una Azure Web App.

### Configuración del CI/CD

1. **Configuración de GitHub Actions**:
   - El archivo de flujo de trabajo se encuentra en `.github/workflows/ci-cd.yml`.
   - Ejecuta pruebas automáticamente y despliega la aplicación en Azure Web App al realizar un push o pull request en la rama `main`.

2. **Configuración de Azure Web App**:
   - Crea una Azure Web App con el runtime **Python 3.11**.
   - Descarga el perfil de publicación y configúralo como un secreto en GitHub (`AZURE_WEBAPP_PUBLISH_PROFILE`).

3. **Despliegue Automático**:
   - Los cambios en la rama `main` activan el flujo de trabajo de GitHub Actions.
   - La aplicación se despliega automáticamente en la Azure Web App configurada.

### Monitoreo y Gestión

- Utiliza el portal de Azure para monitorear el estado de la Web App.
- Los logs de GitHub Actions están disponibles en la pestaña **Actions** del repositorio.

### Mejoras Continuas

- Optimiza el flujo de trabajo de CI/CD ajustando los pasos según las necesidades del proyecto.
- Implementa pruebas adicionales para garantizar la calidad del código.

## Nuevas funcionalidades

### Registro y Login de Usuarios

- **POST /auth/register**: Registra un nuevo usuario.
- **POST /auth/login**: Autentica un usuario y devuelve un JWT.

### Requisitos de acceso

- **Rutas GET**: Requieren un JWT válido.
- **Rutas POST/PUT**: Requieren un JWT válido y que el usuario sea de tipo `Admin`.

## Autenticación con Google (SSO)

### Configuración

1. Registra tu aplicación en Google Cloud Platform.
2. Configura las credenciales OAuth 2.0 y obtén el **Client ID** y el **Client Secret**.
3. Agrega los valores al archivo `.env`:
   ```plaintext
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret
   ```

### Rutas

- **GET /auth/google/login**: Redirige al usuario al flujo de autenticación de Google.
- **GET /auth/google/callback**: Maneja el callback de Google y registra o autentica al usuario.

## Frontend Integrado

Este proyecto incluye un pequeño frontend integrado utilizando **Jinja2** para facilitar la interacción con las funcionalidades de la API. El frontend permite probar las siguientes características:

### Funcionalidades disponibles en el frontend

1. **Inicio**:
   - Página de bienvenida con enlaces de navegación.
   - URL: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

2. **Gestión de personajes**:
   - Listar todos los personajes con sus atributos (`Name`, `Height`, `Mass`, `Hair Color`, `Skin Color`, `Eye Color`).
   - Agregar nuevos personajes mediante un formulario.
   - URL: [http://127.0.0.1:8000/characters](http://127.0.0.1:8000/characters)

3. **Inicio de sesión**:
   - Formulario para iniciar sesión con un usuario registrado.
   - URL: [http://127.0.0.1:8000/auth/login](http://127.0.0.1:8000/auth/login)

4. **Inicio de sesión con Google**:
   - Redirección al flujo de autenticación de Google.
   - URL: [http://127.0.0.1:8000/auth/google/login](http://127.0.0.1:8000/auth/google/login)

### Estructura de las plantillas

Las plantillas HTML están ubicadas en el directorio `templates/` y utilizan **Jinja2** para renderizar contenido dinámico.

```
app/
├── templates/
│   ├── base.html          # Plantilla base con el diseño principal
│   ├── index.html         # Página de inicio
│   ├── characters.html    # Página para listar y agregar personajes
│   ├── login.html         # Página de inicio de sesión
```

### Cómo probar el frontend

1. **Inicia el servidor**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Accede a las páginas en tu navegador**:
   - Página de inicio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Listar y agregar personajes: [http://127.0.0.1:8000/characters](http://127.0.0.1:8000/characters)
   - Formulario de inicio de sesión: [http://127.0.0.1:8000/auth/login](http://127.0.0.1:8000/auth/login)
   - Login con Google: [http://127.0.0.1:8000/auth/google/login](http://127.0.0.1:8000/auth/google/login)

### Notas adicionales

- **Estilos personalizados**: Puedes agregar un directorio `static/` para incluir archivos CSS y JS si deseas personalizar el diseño.
- **Extensibilidad**: Este frontend es básico y puede ser extendido para incluir más funcionalidades según sea necesario.

## Colección de Postman

Para facilitar las pruebas de la API, se incluye una colección de Postman en el archivo `collection.json`. Puedes importarla en Postman siguiendo estos pasos:

1. Abre Postman.
2. Haz clic en **Importar**.
3. Selecciona el archivo `collection.json` ubicado en la raíz del proyecto.
4. Una vez importada, podrás probar las rutas de la API directamente desde Postman.

### Rutas incluidas en la colección

1. **Registro de usuarios**:
   - **POST /auth/register**: Registra un nuevo usuario.

2. **Inicio de sesión**:
   - **POST /auth/login**: Autentica un usuario y devuelve un JWT.

3. **Autenticación con Google**:
   - **GET /auth/google/login**: Redirige al usuario al flujo de autenticación de Google.
   - **GET /auth/google/callback**: Maneja el callback de Google y registra o autentica al usuario.

4. **Gestión de personajes**:
   - **GET /api/characters**: Obtiene todos los personajes.
   - **GET /api/characters/{name}**: Obtiene un personaje por su nombre.
   - **POST /api/characters**: Crea un nuevo personaje.
   - **DELETE /api/characters/{character_id}**: Elimina un personaje por su ID.

5. **Gestión de ítems**:
   - **GET /api/items/getAll**: Obtiene todos los ítems.
   - **GET /api/items/get/{name}**: Obtiene un ítem por su nombre.
   - **POST /api/items/add**: Crea un nuevo ítem.
   - **DELETE /api/items/delete/{id}**: Elimina un ítem por su ID.

### Cómo usar la colección

1. **Configurar variables de entorno en Postman**:
   - Define una variable `{{access_token}}` para almacenar el token JWT obtenido al iniciar sesión.
   - Usa esta variable en el encabezado `Authorization` como `Bearer {{access_token}}`.

2. **Probar las rutas**:
   - Usa las rutas incluidas en la colección para probar las funcionalidades de la API, incluyendo la autenticación con Google.

3. **Notas adicionales**:
   - Asegúrate de que el servidor esté corriendo antes de realizar las pruebas:
     ```bash
     uvicorn main:app --reload
     ```
   - Si estás probando la autenticación con Google, asegúrate de haber configurado correctamente las credenciales en el archivo `.env`.