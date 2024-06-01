from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.base import get_db

from services import user as UserService
from dto import user as UserDTO

router = APIRouter()

@router.post('/', tags=['user'])
async def create(db: Session = Depends(get_db), data: UserDTO.User = None):
    return UserService.create(db=db, data=data)

@router.get('/{id}', tags=['user'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return UserService.get(id=id, db=db)

@router.put('/{id}', tags=['user'])
async def update(id: int = None, db: Session = Depends(get_db), data: UserDTO.User = None):
    return UserService.update(id=id, db=db, data=data)

@router.delete('/{id}', tags=['user'])
async def delete(id: int= None, db: Session = Depends(get_db)):
    return UserService.remove(id=id, db=db)