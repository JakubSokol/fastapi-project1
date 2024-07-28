from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
# from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount("/",StaticFiles(directory=".",html=True),name="static")

# class Item(BaseModel):
#     text: str=None
#     is_done: bool=False


# items=[]

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/")
async def button_click():
    return JSONResponse(content={"message": "Button clicked!"})

# @app.get("/button-click")
# async def button_click():
#     return JSONResponse(content={"message": "Button clicked!"})

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000)





# @app.post("/items")
# def create_item(item: Item):
#     items.append(item)
#     return items


# @app.get("/items",response_model=list[Item])
# def list_items(limit:int=10):
#     return items[0:limit]



# @app.get("/items/{item_id}", response_model=Item)
# def get_item(item_id: int)->Item:
#     if item_id<len(items):
#         return items[item_id]
#     else:
#         raise HTTPException(status_code=404,detail=f"Item{item_id} not found")