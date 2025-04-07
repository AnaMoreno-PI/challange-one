from fastapi import FastAPI, Depends
from api.router import router as api_router
from config import init_db
from config.db_config import SessionLocal, engine
from services.services import CharacterService, AzureCognitiveService


app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
  #if os.getenv('ENVIRONMENT') != "DEVELOP":
  init_db.db_global_init(engine)

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inicializar servicios
def get_character_service(db=Depends(get_db)):
    return CharacterService(db)

def get_azure_cognitive_service():
    # Aquí se pueden pasar las credenciales necesarias para el servicio
    azure_credentials = {"key": "your_key", "endpoint": "your_endpoint"}
    return AzureCognitiveService(azure_credentials)

# Incluir rutas
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
