from pydantic import BaseModel, EmailStr

class UserTypeSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # Cambiar orm_mode a from_attributes

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    user_type_id: int

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    user_type: UserTypeSchema

    class Config:
        from_attributes = True  # Cambiar orm_mode a from_attributes

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
