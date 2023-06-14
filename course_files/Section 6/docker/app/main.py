from fastapi import FastAPI
#pip install fastapi
#pip install uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World. I'm an API!"}
    
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    discount = False

    if item_id > 10:
        discount = True

    
    if q == "manager":
        discount = True
        
    return {"item_id": item_id, "discount": discount, "q": q}