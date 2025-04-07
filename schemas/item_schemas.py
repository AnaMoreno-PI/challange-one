from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: Optional[str]
    skin_color: Optional[str]
    eye_color: Optional[str]

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True  # Habilitar orm_mode para usar from_orm
