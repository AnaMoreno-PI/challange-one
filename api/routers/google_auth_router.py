from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from config.db_config import get_db
from services.user_service import UserService
from schemas.user_schemas import UserResponse
import os

router = APIRouter()

# Configuración de Google OAuth
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8000/auth/google/callback"

if not CLIENT_ID or not CLIENT_SECRET:
    raise RuntimeError("GOOGLE_CLIENT_ID o GOOGLE_CLIENT_SECRET no están configurados correctamente.")

flow = Flow.from_client_config(
    {
        "web": {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": [REDIRECT_URI],
        }
    },
    scopes=["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"],
)

@router.get("/login")
def google_login():
    authorization_url, state = flow.authorization_url(prompt="consent")
    return {"authorization_url": authorization_url}

@router.get("/callback", response_model=UserResponse)
def google_callback(db: Session = Depends(get_db)):
    flow.fetch_token(authorization_response=os.getenv("GOOGLE_AUTH_RESPONSE"))
    credentials = flow.credentials
    request = Request()
    id_info = credentials.id_token

    # Extraer información del usuario
    email = id_info.get("email")
    first_name = id_info.get("given_name")
    last_name = id_info.get("family_name")

    # Crear o actualizar usuario en la base de datos
    user_service = UserService(db)
    user = user_service.create_user({
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "is_google_user": True,
        "password": None,  # Los usuarios de Google no necesitan contraseña
        "user_type_id": 2  # Asignar un tipo de usuario predeterminado, por ejemplo, "User"
    })
    return user
