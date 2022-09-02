from fastapi import APIRouter
from src.endpoints import shopping_cart, home_router

router = APIRouter()

router.include_router(home_router)
router.include_router(shopping_cart.router)
