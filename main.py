from fastapi import FastAPI

# Instantiate app
app = FastAPI()

# Handle get requests to root
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/hello")
def hello(name: str = "Alan"):
    return {"message": f"Hello {name}"}