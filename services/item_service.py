from typing import List, Optional
from schemas.item_schemas import Item, ItemCreate

# Lista en memoria para almacenar los ítems
items_data = [
    {"id": 1, "name": "Luke Skywalker", "height": 172, "mass": 77, "hair_color": "blond", "skin_color": "fair", "eye_color": "blue"},
    {"id": 2, "name": "R2-D2", "height": 96, "mass": 32, "hair_color": "n/a", "skin_color": "blue", "eye_color": "red"},
    # Añadir más ítems según el ejemplo proporcionado
]

# Función para obtener todos los ítems
def get_all_items() -> List[Item]:
    return items_data

# Función para obtener un ítem por nombre
def get_item_by_name(name: str) -> Optional[Item]:
    for item in items_data:
        if item["name"].lower() == name.lower():
            return item
    return None

# Función para agregar un nuevo ítem
def add_item(item: ItemCreate):
    # Verificar que no exista un ítem con el mismo ID
    if any(existing_item["id"] == item.id for existing_item in items_data):
        return None
    items_data.append(item.dict())
    return item

# Función para eliminar un ítem por ID
def delete_item(item_id: int):
    for index, item in enumerate(items_data):
        if item["id"] == item_id:
            del items_data[index]
            return True
    return False
