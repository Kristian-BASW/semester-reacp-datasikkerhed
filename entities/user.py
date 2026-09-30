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