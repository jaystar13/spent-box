from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    name: str
    email: str


class UserRead(UserCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
