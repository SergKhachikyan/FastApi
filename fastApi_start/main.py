from fastapi import FastAPI, HTTPException
from pydantic import Field, BaseModel, EmailStr
import uvicorn

app = FastAPI()

users = [
    {
        "id":1,
        "name":"Alex",
        "email":"alex@mail.ru",
        "age":17,
    },
    {
        "id":2,
        "name":"George",
        "email":"georg@mail.ru",
        "age":20,
    },
]

class User(BaseModel):
    id:int
    name:str = Field(max_length=10)
    email:EmailStr
    age:int = Field(ge = 0, le = 120)

class UserCreate(BaseModel):

    name:str = Field(max_length=10)
    email:EmailStr
    age:int = Field(ge = 0, le = 120)


@app.get("/users")
def get_user():
    return users

@app.get("/users/{id}")
def get_user(id: int):
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404,detail="User not found")

@app.post("/users")
def user_create(user:UserCreate):
    new_id = users[-1]["id"] + 1 if users else 1
    new_user = {"id":new_id,**user.dict()}
    users.append(new_user)
    return new_user

if __name__ == "__main__":
    uvicorn.run("main:app")