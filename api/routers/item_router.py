# app/api/routers/items.py
from fastapi import APIRouter, HTTPException
from typing import List
from schemas.item_schemas import Item, ItemCreate
from services import item_service

router = APIRouter()

@router.get("/items/getAll", response_model=List[Item])
def get_all_items():
    return item_service.get_all_items()

@router.get("/items/get/{name}", response_model=Item)
def get_item_by_name(name: str):
    item = item_service.get_item_by_name(name)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/items/add", response_model=Item)
def add_item(item: ItemCreate):
    new_item = item_service.add_item(item)
    if not new_item:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    return new_item

@router.delete("/items/delete/{id}")
def delete_item(id: int):
    deleted = item_service.delete_item(id)
    if not deleted:
        raise HTTPException(status_code=400, detail="Item not found")
    return {"detail": "Item deleted successfully"}
