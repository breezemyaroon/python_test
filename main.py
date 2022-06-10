import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from action import Action

app = FastAPI()


class User(BaseModel):
    ID: Optional[int]
    username: Optional[str]
    password: Optional[str]
    name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]

class DeleteUser(BaseModel):
    ID: Optional[int]

class chagnePassword(BaseModel):
    ID: Optional[int]
    password: Optional[str]


class login(BaseModel):
    username: Optional[str]
    password: Optional[str]
    
class chagnePasswordAndName(BaseModel):
    id: Optional[int]
    password: Optional[str]
    name: Optional[str]
    
    
    
@app.post("/changePassword_and_Name")
async def chang_pasword(user: chagnePasswordAndName):
    data = Action.changePasswordAndName(user)
    return data


# -----------rout--------------
@app.get("/")
async def read_root():
    return {"Con": "Start"}


@app.get("/hw/get")
async def hw_get():
    data = Action.getHW()
    return data


@app.get("/hw/get_by_id")
async def hw_get_by_id(ID):
    data = Action.getHWByID(ID)
    return data


@app.get("/hw/get_by_name")
async def hw_get_by_name(name):
    data = Action.getHWByName(name)
    return data


@app.get("/hw/add_hw")
async def hw_add_hw(name, hw_name):
    data = Action.addHW(name, hw_name)


@app.get("/hw/update_status_hw")
async def hw_update_status_hw(ID, status):
    data = Action.updateStatusHW(ID, status)
    return data


@app.get("/hw/update_value_hw")
async def hw_update_status_hw(ID, value):
    data = Action.updateValueHW(ID, value)
    return data


@app.get("/hw/delete_hw")
async def hw_update_status_hw(ID):
    data = Action.DeleteHW(ID)
    return data


@app.post("/login")
async def login(user: login):
    data = Action.login(user)
    return data

@app.post("/register")
async def registers(user: User):
    data = Action.register(user)
    return data

@app.post("/chang_pasword")
async def chang_pasword(user: chagnePassword):
    data = Action.changePassword(user)
    return data

@app.post("/delete_user")
async def delete_user(user: DeleteUser):
    data = Action.deleteUser(user)
    return data


@app.get("/hw/updata_hardware")
async def updata_hardware(status,value,id):
    data = Action.updata_hardware(status,value,id)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="192.168.43.48", port=8000)