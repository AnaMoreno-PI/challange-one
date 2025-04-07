from sqlalchemy import Column, Integer, String
from config.db_config import Base
from api.models.characters import BaseModel

class Item(BaseModel):
    __tablename__ = "items"

    name = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=True)
    skin_color = Column(String, nullable=True)
    eye_color = Column(String, nullable=True)
