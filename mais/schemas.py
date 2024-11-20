from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserSchema(BaseModel):
    username: str
    password: str
    email: EmailStr


class UseDatabase(UserSchema):
    id: int
