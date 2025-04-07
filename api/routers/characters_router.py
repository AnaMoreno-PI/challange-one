from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.item_schemas import Item, ItemCreate
from services.character_services import CharacterService
from typing import List
from config.db_config import get_db

router = APIRouter()

@router.get("/characters", response_model=List[Item])
def read_characters(db: Session = Depends(get_db)):
    service = CharacterService(db)
    characters = service.get_all_characters()
    return [Item.from_orm(character) for character in characters]  # Convertir a modelos Pydantic

@router.get("/characters/{name}", response_model=Item)
def read_character_by_name(name: str, db: Session = Depends(get_db)):
    service = CharacterService(db)
    character = service.get_character_by_name(name)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return Item.from_orm(character)  # Convertir a modelo Pydantic

@router.post("/characters", response_model=Item)
def create_character_endpoint(item: ItemCreate, db: Session = Depends(get_db)):
    service = CharacterService(db)
    character = service.create_character(item.dict())
    return Item.from_orm(character)  # Convertir a modelo Pydantic

@router.delete("/characters/{character_id}")
def delete_character_endpoint(character_id: int, db: Session = Depends(get_db)):
    service = CharacterService(db)
    success = service.delete_character(character_id)
    if not success:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"detail": "Character deleted successfully"}