import uuid
from typing import Optional

from fastapi_users import schemas


# class UserRead(schemas.BaseUser[uuid.UUID]):
class UserRead(schemas.BaseUser[int]):
    # pass
    id: int
    email: str
    username: str
    role_id: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True

class UserCreate(schemas.BaseUserCreate):
    username: str                                # taken from our user_model
    role_id: int
    email: str                                   # copied from BaseUserCreate
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


"""
will not use update  in our app
class UserUpdate(schemas.BaseUserUpdate):
    pass
"""
