## user file 

from .. import models, schemas , utils
from fastapi import status, HTTPException, Depends, APIRouter
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post('/',status_code= status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):
    
    
    # has the passsword 
    
    hash_pass = utils.getHash(user.password)
    user.password = hash_pass
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    #for return the value
    return new_user


@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id:int,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No user found with user id {id}")
       
    return user
