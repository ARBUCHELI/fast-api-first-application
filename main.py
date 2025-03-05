from fastapi import FastAPI, HTTPException
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

'''
@app.delete("/items")
def delete_item(item: Item):
    name = item.name
    # Delete the item
    items.remove(name)
    return {}
'''
@app.delete("/items")
# Make asynchronous
async def root(item: Item):
    name = item.name
    # Check if name is in items
    if name not in items:
        # Return the status code for not found
        raise HTTPException(status_code=404, detail="Item not found.")
    await items.remove(name)
    return {"message": "Item deleted"}