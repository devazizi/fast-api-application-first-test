from .db import session_maker
from src.store.models import ShoppingCart, ShoppingCartItem, ProductVariation, Product, ProductCategory


def get_user_shopping_cart(user_id: int):

    response = session_maker()\
        .query(ShoppingCart)\
        .join(ShoppingCartItem)\
        .join(ProductVariation)\
        .join(Product)\
        .join(ProductCategory)\
        .filter(ShoppingCart.user_id==user_id)\
        .first()

    shopping_cart_items = []
    for shopping_cart_item in response.shopping_cart_items:
        shopping_cart_items.append({
            'product_variation_id': shopping_cart_item.product_variation_id,
            'quantity': shopping_cart_item.quantity,
            'shopping_cart_item_id': shopping_cart_item.id,
            'created_at': shopping_cart_item.created_at,
            'updated_at': shopping_cart_item.updated_at,
            'product_variation': {
                'id': shopping_cart_item.product_variation.id,
                'name': shopping_cart_item.product_variation.name,
                'price': shopping_cart_item.product_variation.price,
                'stock': shopping_cart_item.product_variation.stock,
                'created_at': shopping_cart_item.product_variation.created_at,
                'updated_at': shopping_cart_item.product_variation.updated_at,
                'product': {
                    'id': shopping_cart_item.product_variation.product.id,
                    'name': shopping_cart_item.product_variation.product.name,
                    'description': shopping_cart_item.product_variation.product.description,
                    'created_at': shopping_cart_item.product_variation.product.created_at,
                    'updated_at': shopping_cart_item.product_variation.product.updated_at,
                    'product_category': {
                        'id': shopping_cart_item.product_variation.product.product_category.id,
                        'name': shopping_cart_item.product_variation.product.product_category.name,
                        'description': shopping_cart_item.product_variation.product.product_category.description,
                        'created_at': shopping_cart_item.product_variation.product.product_category.created_at,
                        'updated_at': shopping_cart_item.product_variation.product.product_category.updated_at,
                    }
                }
            }
        })

    return {
        'id': response.id,
        'shopping_cart_items': shopping_cart_items
    }

