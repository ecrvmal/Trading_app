from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, Request, status
from pydantic import BaseModel, Field
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI(
    title="Trading App"
)


# Благодаря этой функции клиент видит ошибки, происходящие на сервере,
# вместо "Internal server error"
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),          # client will see error detail
    )



fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]

class DegreeType(BaseModel):
    newbie = "newbie"
    expert = "expert"

class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType     #  newbie | expert  if else > error

class User(BaseModel):
    id: int
    role: str
    name: str
    degree: list[Degree]



@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

# request : http://127.0.0.1:8000/users/2
# [{"id":2,"role":"investor","name":"John"}]


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]

# http://127.0.0.1:8000/trades?limit=1
# [{"id":1,"user_id":1,"currency":"BTC","side":"buy","price":123,"amount":2.12}]
# http://127.0.0.1:8000/trades?limit=1&offset=1
# [{"id":2,"user_id":1,"currency":"BTC","side":"sell","price":125,"amount":2.12}]



fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]



@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}



# to describe Trade we use data model (Pydentic)
class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: int


@app.post("/trades")
def add_trades(trades: List[Trade]):   # input : list of deals
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}


