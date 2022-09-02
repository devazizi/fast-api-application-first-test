from fastapi import APIRouter
# from src.store.auth import LoginRequest
from src.store.repository import get_user_shopping_cart
from fastapi.encoders import jsonable_encoder


router = APIRouter(
    prefix="/api/v1",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)


@router.get('/shopping-carts')
def login():

    data = get_user_shopping_cart(user_id=1)

    shopping_cart_total_price = 0
    for shopping_cart_item in data['shopping_cart_items']:

        shopping_cart_total_price += shopping_cart_item['product_variation']['price'] * shopping_cart_item['quantity']

    data['total_shopping_cart_price'] = shopping_cart_total_price

    return {
        "description": "Ok",
        'data': data
    }