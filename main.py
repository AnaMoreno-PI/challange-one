from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from api.router import router as api_router
from config import init_db
from config.db_config import SessionLocal, engine
from services.character_services import CharacterService
from services.user_service import UserService
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI()

# Configurar plantillas
templates = Jinja2Templates(directory="e:/PI/Challange/Etapa 6/app/templates")

@app.middleware("http")
async def set_secure_headers(request: Request, call_next):
    response = await call_next(request)
    # Configurar encabezados de seguridad manualmente
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "no-referrer"
    return response

# Configurar rate limiting
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(429)
async def rate_limit_exceeded_handler(request: Request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Try again later."},
    )

@app.on_event("startup")
async def startup_db_client():
    """Inicializa la base de datos al iniciar la aplicación."""
    init_db.db_global_init(engine)

# Dependencia para obtener la sesión de base de datos
def get_db():
    """Proporciona una sesión de base de datos para las operaciones."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(request: Request):
    """Ruta de inicio."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/characters")
@limiter.limit("5/minute")  # Máximo 5 solicitudes por minuto
def list_characters(request: Request, db: Session = Depends(get_db)):
    """Lista todos los personajes."""
    characters = CharacterService(db).get_all_characters()
    return templates.TemplateResponse("characters.html", {"request": request, "characters": characters})

@app.post("/characters")
def add_character(
    name: str = Form(...),
    height: int = Form(...),
    mass: int = Form(...),
    hair_color: str = Form(None),
    skin_color: str = Form(None),
    eye_color: str = Form(None),
    db: Session = Depends(get_db),
):
    """Agrega un nuevo personaje."""
    CharacterService(db).create_character({
        "name": name,
        "height": height,
        "mass": mass,
        "hair_color": hair_color,
        "skin_color": skin_color,
        "eye_color": eye_color,
    })
    return RedirectResponse(url="/characters", status_code=303)

@app.get("/auth/login")
def show_login_form(request: Request):
    """Muestra el formulario de inicio de sesión."""
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/auth/login")
@limiter.limit("3/minute")  # Máximo 3 intentos de inicio de sesión por minuto
def login_user(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    """Maneja el inicio de sesión del usuario."""
    user_service = UserService(db)
    user = user_service.authenticate_user(email, password)
    if not user:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})
    access_token = user_service.create_access_token(user)
    response = RedirectResponse(url="/", status_code=303)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return response

# Incluir rutas de la API
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)