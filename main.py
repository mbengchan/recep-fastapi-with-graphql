from fastapi import FastAPI

app = FastAPI()

cars = ["Tesla", "Toyota", "Mazda", "Buggatti"]

@app.get('/')
def read_root():
    return "Hello World"

@app.get('/cars')
def listCars():
    return cars

@app.get('/cars/:id')
def get_car(id: int):
    return cars[id]

@app.post('/car')
def createCar():
    return "Car created"

@app.put('/car/:id')
def deleteCar(id: int):
    return "Car Deleted"

@app.patch('/car/:id')
def deleteCar(id: int):
    return "Car Deleted"

@app.delete('/car/:id')
def deleteCar(id: int):
    return "Car Deleted"

