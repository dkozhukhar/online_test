from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample products
products = [
    {"id": 1, "name": "Minimalist T-Shirt", "price": 20.0},
    {"id": 2, "name": "Stylish Backpack", "price": 50.0},
    {"id": 3, "name": "Eco Water Bottle", "price": 15.0},
]

cart = []

class CartItem(BaseModel):
    product_id: int
    quantity: int

@app.get("/products")
def get_products():
    return products

@app.post("/cart")
def add_to_cart(item: CartItem):
    cart.append(item.dict())
    return {"message": "Added to cart", "cart": cart}

@app.get("/cart")
def view_cart():
    return cart
