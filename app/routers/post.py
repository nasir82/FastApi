from .. import models, schemas , oauth2
from fastapi import Response, status, HTTPException, Depends, APIRouter
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List


router = APIRouter(
    tags=['Posts']
)


'''@router.get('/sqlalchemy',response_model=List[schemas.Post])
def test_posts(db:Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return post
    
'''
"""
                    @router.post('/createposts')
                    def create_post(payload: dict = Body(...)):
                        return {"new_post": f" name {payload['name']} email {payload['email']} and reg {payload['reg']}"}
"""
@router.post('/posts',status_code= status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(post:schemas.PostBase,db:Session = Depends(get_db), get_current_user:int = Depends(oauth2.get_current_user)):
    
    # this codes are getting easiar using sqlalchemy
    # just wring python code and this will generate database query
    
    # new_post = models.post(**post.dict())
    
    new_post = models.Post(owner_id = get_current_user.id ,**post.model_dump())  #post variable
    db.add(new_post)
    db.commit() # like normal commit
    db.refresh(new_post) #for return the value
    return new_post
"""print(post.model_dump())
    if not post:
        return 
    
    conn.commit()
    new_post = cursor.fetchone()
    return {"data": new_post} 
"""

@router.get('/posts',response_model=List[schemas.Post])
def get_posts(db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user), limit: int = 10, skip:int = 0):
    print(limit)
    post = db.query(models.Post).limit(limit).offset(skip).all()
    return post



'''
                    pain to get value
                    any format data
                    data is not getting validate
                    schema set a pattern

                    using pydantic schema validate kore 

'''


'''
                    title str
                    content str
                    category 
                    boolean

'''
        
        
@router.get("/posts/{id}",response_model=schemas.Post)
def get_post(id:int , response:Response, db:Session = Depends(get_db)):
    '''
    print(type(id))
    post = find_post(int(id))
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": "post not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with {id} not found")
    
    
    cursor.execute("""select * from posts where id = %s """,(str(id)))
    post_status = cursor.fetchone()
    return {"post_details": post_status}
    '''
    post = db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with {id} not found")
    
    return post
    
       

@router.delete('/posts/{id}',status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    # deleting post
    #find the index in the post that need to delete
    # my_posts.pop(inded)
   
    post = db.query(models.Post).filter(models.Post.id==id)
    post_el = post.first()
    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
    if post_el.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Non authorized to perform request action")
    post.delete(synchronize_session=False)
    db.commit()
    

"""    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no post available for this id")
    # return {"message" : 'post succesfully deleted'} not better choice
    return Response(status_code=status.HTTP_204_NO_CONTENT) # this is staturd aproach"""


## update 

@router.put('/posts/{id}')
def update_post(id:int, post:schemas.Post,db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    
    post_query = db.query(models.post).filter(models.Post.id==id)
    post_el = post.first()
    if post.first()==None:
        raise HTTPException()
    
    if post_el.owner_id != oauth2.get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Non authorized to perform request action")
    
    post.update( post.dict(),synchronize_session= False)
    db.commit()
    return post_query.first()
    
    
'''    index = find_index_of_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no such post")
    
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index]= post_dict
    return {"data": post_dict}'''
