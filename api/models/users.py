from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from config.db_config import Base

class UserType(Base):
    __tablename__ = "user_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=True)  # Puede ser NULL para usuarios autenticados con Google
    user_type_id = Column(Integer, ForeignKey("user_types.id"), nullable=True)
    is_google_user = Column(Boolean, default=False)  # Indica si el usuario se autenticó con Google

    user_type = relationship("UserType")
