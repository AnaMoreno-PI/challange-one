from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: int
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str

class ItemCreate(Item):
    pass
