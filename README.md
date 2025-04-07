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

2. Crea un entorno virtual (opcional pero recomendado):
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instala las dependencias del proyecto:
pip install -r requirements.txt

4. Configura las variables de entorno en el archivo .env:
DB_NAME=
DB_UID=
DB_PASS=
DB_PORT=
DB_SERVER=
ENVIRONMENT=

Ejecución del proyecto
Inicia el servidor de desarrollo:

Accede a la documentación interactiva de la API en tu navegador:

Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

Estructura del proyecto

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