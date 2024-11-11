from fastapi import HTTPException, status
from .. import models, schemas
from ..hashing import Hash
from sqlalchemy.orm import Session


def create(request: schemas.User, db: Session):
    new_user = models.Users(name=request.name,
                            email=request.email,
                            password=Hash.encrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id: int, db: Session):
    user = db.query(models.Users).where(models.Users.user_id == id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with user id {id} not found')