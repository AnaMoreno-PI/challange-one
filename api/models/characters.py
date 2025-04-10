from sqlalchemy import Column, Integer, String
from config.db_config import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=True)
    skin_color = Column(String, nullable=True)
    eye_color = Column(String, nullable=True)

