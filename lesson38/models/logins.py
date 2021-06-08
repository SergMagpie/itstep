from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str


class UserCreate(BaseUser):
    password: str


class ModelUser(BaseUser):
    id: int

    class Config:
        orm_mode = True
