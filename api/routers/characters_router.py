from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.item_schemas import Item, ItemCreate
from services import character_services
from typing import List
from config.db_config import get_db


router = APIRouter()


@router.get("/characters", response_model=List[Item])
def read_characters(db: Session = Depends(get_db)):
    return character_services.get_characters(db)

# Ruta para obtener un character por nombre
@router.get("/characters/{name}", response_model=Item)
def read_character_by_name(name: str, db: Session = Depends(get_db)):
    character = character_services.get_character_by_name(db, name)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

# Ruta para crear un nuevo character
@router.post("/characters", response_model=Item)
def create_character(item: ItemCreate, db: Session = Depends(get_db)):
    return character_services.create_character(db, item)

# Ruta para eliminar un character por id
@router.delete("/characters/{character_id}")
def delete_character(character_id: int, db: Session = Depends(get_db)):
    success = character_services.delete_character(db, character_id)
    if not success:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"detail": "Character deleted successfully"}