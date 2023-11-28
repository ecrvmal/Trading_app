from fastapi import FastAPI
import redis

app = FastAPI(
    title="Trading App"
)

r = redis.Redis(host='redis', port=6379, decode_responses=True)

fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    redis_key = f'redis_user_{user_id}'
    print(redis_key)
    res = r.hgetall(redis_key)
    return {redis_key: res}

# request : http://127.0.0.1:8000/users/1
# responce
# Code	200
# Details : Response body : {"redis_user_1": {"role": "Admin", "name": "Ann_m"}}


@app.post("/users/{user_id}")
def change_user_name(user_id: int, role: str, new_name: str):
    redis_key = f'redis_user_{user_id}'
    data = {"role": role, "name": new_name}
    res1 = r.hset(redis_key, mapping=data)
    # print(res1)
    return {"status": 200, redis_key: data}

# http://127.0.0.1:8000/users/1?role=Admin&new_name=Ann_m
# response: Code	 200
# Details Response body
# Download { "status": 200, "redis_user_1": {"role": "Admin", "name": "Ann_m" }}



