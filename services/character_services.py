from sqlalchemy.orm import Session
from schemas.item_schemas import ItemCreate
from api.models.characters import Character

def get_characters(db: Session):
    return db.query(Character).all()

def get_character_by_name(db: Session, name: str):
    return db.query(Character).filter(Character.name == name).first()

def create_character(db: Session, item: ItemCreate):
    db_character = Character(
        id=item.id, 
        name=item.name,
        height=item.height,
        mass=item.mass,
        hair_color=item.hair_color,
        skin_color=item.skin_color,
        eye_color=item.eye_color
    )
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

def delete_character(db: Session, character_id: int):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if db_character:
        db.delete(db_character)
        db.commit()
        return True
    return False