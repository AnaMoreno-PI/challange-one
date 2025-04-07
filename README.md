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