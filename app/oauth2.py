from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends,status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import database, models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


# secret key
# algorithm
# expriation time


SECRET_KEY = "dfjal34kh325j245h2h2hklfhlk4542tjk542kljffer435fd4td"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire  = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def verify_access_token(token:str, creadentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        
        id:str = payload.get("user_id")
        if id is None:
            raise creadentials_exception
        
        token_data = schemas.TokenData(id=id)
    except JWTError:
         raise creadentials_exception
    return token_data
     
def get_current_user(token:str = Depends(oauth2_scheme),db:Session = Depends(database.get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"could not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    
    verified_token = verify_access_token(token=token, creadentials_exception=credential_exception)
    user = db.query(models.User).filter(models.User.id == verified_token.id).first()
    
    return user

