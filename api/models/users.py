from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base

class UserType(Base):
    __tablename__ = "user_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)  # Cambiar VARCHAR(MAX) a VARCHAR(255)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)  # Cambiar VARCHAR(MAX) a VARCHAR(255)
    last_name = Column(String(255), nullable=False)   # Cambiar VARCHAR(MAX) a VARCHAR(255)
    email = Column(String(255), unique=True, nullable=False)  # Cambiar VARCHAR(MAX) a VARCHAR(255)
    password = Column(String(255), nullable=False)    # Cambiar VARCHAR(MAX) a VARCHAR(255)
    user_type_id = Column(Integer, ForeignKey("user_types.id"), nullable=False)

    user_type = relationship("UserType")
