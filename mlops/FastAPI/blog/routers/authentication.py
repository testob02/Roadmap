from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Authentication'],
    prefix='/login'
)


get_db = database.get_db


@router.post('/', response_model=schemas.Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Users).where(models.Users.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Invalid Credentials')
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Incorrect Password')
    
    access_token = token.create_access_token(
        data={'sub': user.email}
    )
    
    return {"access_token": access_token, "token_type":"bearer"}