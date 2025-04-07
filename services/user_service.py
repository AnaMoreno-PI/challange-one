from sqlalchemy.orm import Session
from api.models.users import User, UserType
from schemas.user_schemas import UserCreate
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from config.db_config import SECRET_KEY

class UserService:
    SECRET_KEY = SECRET_KEY
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def __init__(self, db: Session):
        self.db = db
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def authenticate_user(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user or not self.verify_password(password, user.password):
            return None
        return user

    def create_access_token(self, user: User):
        to_encode = {"sub": user.email, "user_type": user.user_type.name}
        expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
