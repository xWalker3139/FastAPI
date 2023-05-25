from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# CRUD = Create, Read, Update, Delete
# GET, POST, PUT, DELETE

class Item(BaseModel):
    nume: str
    pret: int

class UpdateItem(BaseModel):
    nume: Optional[str] = None
    pret: Optional[int] = None

cars = {
    1:{
        "nume":"Volvo",
        "pret":3400
    },
    2:{
        "nume":"Audi",
        "pret":4000,
    }
}

@app.get('/')
def acasa():
    return {"Mesaj":"Salutare lume!"}

@app.get('/contact')
def contact():
    return {"Contact":"Aceasta este pagina de contact"}

@app.get('/get_car/{item_id}')
def get_car(item_id: int):
    return cars[item_id]

@app.post('/create_car/{item_id}')
def create_car(item_id: int, item: Item):
    if item_id in cars:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Acest ID nu a fost gasit")
    cars[item_id] = {"nume":item.nume, "pret":item.pret}
    return cars[item_id]

@app.delete('/delete-car/')
def delete_car(item_id: int):
    if item_id not in cars:
        return HTTPException(status_code=404, detail="Acest ID nu a fost gasit")
    del cars[item_id]
    return HTTPException(status_code=200)

@app.put('/update_cars/{item_id}')
def update_cars(item_id: int, item: UpdateItem):
    if item_id not in cars:
        return HTTPException(status_code=404, detail="Acest ID nu a fost gasit")
    if item.nume != None:
        cars[item_id]["nume"] = item.nume
    if item.pret != None:
        cars[item_id]["pret"] = item.pret
    return cars[item_id]