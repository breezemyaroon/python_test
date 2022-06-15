#from typing import Union

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/my_name")
def my_name():
    data = "AROON WANTHONG"
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data

@app.get("/input_name_Lastname")
def input_name_Lastname(fristname,lastname):
    data = fristname + " " + lastname
    return data

@app.get("/velocity")
def velocity(S:float,T:float):
    vel = "velcolcity {:.2f}".format(S/T)
    return vel

@app.get("/paralel-sereis_Cricuit")
def paralel(R1:float, R2:float, R3:float):
    resistence = "Paralel {:.2f}".format(((1/R1)+(1/R2)+(1/R3))**-1),"Sereis {:.2f}".format((R1)+(R2)+(R3))
    return resistence


if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.43.48", port=8000, reload=True)