import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

if os.getenv('ENVIRONMENT') != 'PRODUCTION':
    load_dotenv()

# Obtener las credenciales de la base de datos desde las variables de entorno
DB_SERVER = os.getenv('DB_SERVER')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_UID = os.getenv('DB_UID')
DB_PASS = os.getenv('DB_PASS')

# Construir la cadena de conexión
DATABASE_URL = urllib.parse.quote_plus(
    f'Driver={{ODBC Driver 17 for SQL Server}};'
    f'Server={DB_SERVER},{DB_PORT};'
    f'Database={DB_NAME};'
    f'Uid={DB_UID};'
    f'Pwd={DB_PASS};'
    f'Encrypt=yes;'
    f'TrustServerCertificate=no;'
    f'Connection Timeout=30;'
)
CONNECTION_STR = f'mssql+pyodbc:///?odbc_connect={DATABASE_URL}'

# Crear el motor de la base de datos
engine = create_engine(CONNECTION_STR, echo=True)

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    """
    Proporciona una sesión de base de datos para las operaciones.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")  # Usa un valor por defecto solo para desarrollo
