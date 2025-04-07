# app/api/main_router.py
from fastapi import APIRouter
from api.routers import item_router, characters_router
from api.routers import auth_router

router = APIRouter()

# Incluir las rutas del módulo de ítems
router.include_router(item_router.router, prefix="/api", tags=["items"])
router.include_router(characters_router.router, prefix="/api", tags=["character"])
router.include_router(auth_router.router, prefix="/auth", tags=["auth"])

# router.include_router(another_router.router, prefix="/api/another", tags=["another"])
