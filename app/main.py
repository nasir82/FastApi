from fastapi import Body, FastAPI
from .routers import user
from . import models
from .database import  engine
from .routers import post, user, auth
from .config import settings


models.Base.metadata.create_all (bind= engine)

app = FastAPI()

# this is pydantic model

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

    
@app.get('/')  # this is a decorator define request type and path !operator get() is an api method
async def root(): # name doesn't matter
    return {"message": "Hellow world !!!"}








