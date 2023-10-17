from typing import Union
import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    name: str
    location: Optional[str]
    id: int

def GET_USERS():
    with open("users.json","r") as file:
        USERS = json.load(file)
    return USERS

def UPDATE_USERS(USERS):
    with open("users.json","w") as file:
        json.dump(USERS, file)
    
@app.get("/")
async def read_root():
    # Base endpoint for health check
    return {"status":"Success"}

@app.get("/user/profile/{user_id}")
async def get_user_profile(user_id: int):
    USERS = GET_USERS()
    user = [u for u in USERS if u["id"] == user_id]
    if len(user)== 0:
        raise HTTPException(404,"User not found")
    return user[0]

@app.get("/user/list")
async def get_user_list():
    USERS = GET_USERS()
    return USERS

@app.post("/user/create")
async def create_user(user: User):
    USERS = GET_USERS()
    user_id = len(USERS) + 1
    user = {"id":user_id, "name": user.name, "location": user.location}
    USERS.append(user)
    UPDATE_USERS(USERS)
    return user
