from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    
class UserInfo(BaseModel):
    username: str
    password: str
    fullname: str
    phone: str
    age: int

class UserInDB(User):
    hashed_password: str
    
    
class UserProfile(BaseModel):
    username: str
    fullname: str
    phone: str
    age: int
    
class UserUpdate(BaseModel):
    fullname: str
    phone: str
    age: int