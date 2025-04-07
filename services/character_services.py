from sqlalchemy.orm import Session
from api.models.characters import Character
from schemas.item_schemas import ItemCreate


class CharacterService:
    """Servicio para manejar la lógica relacionada con personajes."""

    def __init__(self, db: Session):
        self.db = db

    def get_all_characters(self):
        """Obtiene todos los personajes."""
        return self.db.query(Character).all()

    def get_character_by_name(self, name: str):
        """Obtiene un personaje por su nombre."""
        return self.db.query(Character).filter(Character.name == name).first()

    def create_character(self, item: dict):
        """Crea un nuevo personaje."""
        character = Character(
            name=item["name"],
            height=item["height"],
            mass=item["mass"],
            hair_color=item.get("hair_color"),
            skin_color=item.get("skin_color"),
            eye_color=item.get("eye_color"),
        )
        self.db.add(character)
        self.db.commit()
        self.db.refresh(character)
        return character

    def delete_character(self, character_id: int):
        """Elimina un personaje por su ID."""
        character = self.db.query(Character).filter(Character.id == character_id).first()
        if character:
            self.db.delete(character)
            self.db.commit()
            return True
        return False