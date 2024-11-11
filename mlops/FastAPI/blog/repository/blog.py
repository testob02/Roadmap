from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id: int,db: Session):
    blog = db.query(models.Blog).where(models.Blog.id == id)
    if blog.first():
        blog.delete(synchronize_session=False)
        db.commit()
        return 'deleted'
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} does not exist")


def update(id: int,request: schemas.Blog,db: Session):
    blog = db.query(models.Blog).where(models.Blog.id == id)
    if blog.first():
        blog.update({models.Blog.title:request.title,
                     models.Blog.body:request.body}, synchronize_session=False)
        db.commit()
        return 'updated'
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} does not exist")
   
    
def show(id: int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} does not exist")
    return blog

   