from fastapi import APIRouter, Depends
from .. import schemas, database
from ..repository import user
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Users'],
    prefix='/user'
)



get_db = database.get_db



@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)
    


@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.get(id, db)
