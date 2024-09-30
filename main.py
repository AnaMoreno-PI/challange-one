from fastapi import FastAPI
from api.router import router as api_router
from config import init_db
from config.db_config import SessionLocal
from config.db_config import engine
import os


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

# Incluir rutas
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
