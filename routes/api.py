from fastapi import APIRouter
from src.endpoints import shopping_cart

router = APIRouter()

router.include_router(shopping_cart.router)