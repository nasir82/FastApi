

from datetime import datetime
from pydantic import BaseModel,EmailStr
from typing import Optional

'''
class Post(BaseModel):
    id:int
    title:str
    content:str
    published: bool = True
    owner_id:int
    
class PostBase(BaseModel):
    title:str
    content:str
    published: bool = True
    
class CreatePost(PostBase):
    title:str
    content:str
    published: bool = True
    
class UpdatePost(PostBase):
    pass
    

class PostRespone(BaseModel):
    title:str
    content:str
    published:bool
    class config:
        orm_mode = True
        
        
        
class UserCreate(BaseModel):
    email:EmailStr
    password:str
    
class UserResponse(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        orm_mode = True
        
        
        
class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
    
class Token(BaseModel):
    access_token:str
    token_type:str
    

class TokenData(BaseModel):
    id: Optional[int] = None
    
    
      
'''
class UserOut(BaseModel):
    email:EmailStr
    password:str
    created_at:datetime
    
    class Config:
        orm_mode= True
        
class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True
    
    
    
class PostCreate(PostBase):
    pass
    
    
class Post(PostBase):
    id:int
    created_at:datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        orm_mode = True
        
        
        
class UserCreate(BaseModel):
    email:EmailStr
    password:str
    
  
class UserLogin(BaseModel):
    email:EmailStr
    password:str
      
class Token(BaseModel):
    access_token:str
    token_type:str
    

class TokenData(BaseModel):
    id: Optional[int] = None
    
