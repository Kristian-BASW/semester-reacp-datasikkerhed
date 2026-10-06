from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    firstname: str
    lastname: str
    cpr_number: str
    
    
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    cpr_number: str
    
class UserResponse(BaseModel):
    username: str
    firstname: str
    lastname: str
    cpr_number: str
    
class UserResponseList(BaseModel):
    username: str
    firstname: str
    lastname: str
    
class UserResponseRaw(BaseModel):
    username: str
    firstname: str
    lastname: str
    cpr_number_encrypted: str