from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    national_code = Column(String)
    cell_number = Column(String)
    password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    # updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    # author_id = Column(Integer, ForeignKey('author.id'))
    shopping_cart = relationship('ShoppingCart', uselist=False)
    # author = relationship('Author')


class ShoppingCart(Base):
    __tablename__ = 'shopping_carts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    shopping_cart_items = relationship('ShoppingCartItem')


class ShoppingCartItem(Base):
    __tablename__ = 'shopping_cart_items'
    id = Column(Integer, primary_key=True, index=True)
    shopping_cart_id = Column(Integer, ForeignKey('shopping_carts.id'))
    product_variation_id = Column(Integer, ForeignKey('product_variations.id'))
    quantity = Column(Integer)
    # product_variation_id = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    product_variation = relationship('ProductVariation', uselist=False)


class ProductVariation(Base):
    __tablename__ = 'product_variations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))
    price = Column(Integer)
    stock = Column(Integer)
    # product_variation_id = Column(Integer)
    #
    product = relationship('Product', uselist=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    product_category_id = Column(Integer, ForeignKey('product_categories.id'))
    product_category = relationship('ProductCategory', uselist=False)


class ProductCategory(Base):
    __tablename__ = 'product_categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
