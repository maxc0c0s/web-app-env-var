from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"MESSAGE": os.getenv("MESSAGE")}
