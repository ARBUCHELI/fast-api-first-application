from fastapi import FastAPI
#from datetime import date
from pydantic import BaseModel
# Define model Item
'''class Item(BaseModel):
    name: str
    quantity: int = 0
    expiration: date = None
'''
# Define model Item
'''class Item(BaseModel):
    name: str
    description: str
'''
class Item(BaseModel):
    name: str
# Define items at application start
#items = {"bananas": "Yellow fruit."}
items = {"apples", "oranges", "bananas"}
# Instantiate app
app = FastAPI()

# Handle get requests to root
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/hello")
def hello(name: str = "Alan"):
    return {"message": f"Hello {name}"}

@app.post("/")
def root(item: Item):
    name = item.name
    return {"message": f"We have {name}"}


@app.put("/items")
def update_item(item: Item):
    name = item.name
    # Update the description
    items[name] = item.description
    return item

@app.delete("/items")
def delete_item(item: Item):
    name = item.name
    # Delete the item
    items.remove(name)
    return {}