from database.models import User
from sqlalchemy.orm import Session
from dto import user

def create(data: user.User, db: Session):
    user = User(name=data.name)

    try:
        db.add(user)
        db.commit()
        db.refresh()
    except Exception as e:
        print(f"Ошибка: {e}")

    return user
        

def get(id: int, db: Session):

    return db.query(User).filter(User.id==id).first()

def update(data: user.User, db: Session, id: int):

    user = db.query(User).filter(User.id==id).first()
    user.name = data.name

    db.add(user)
    db.commit()
    db.refresh()

    return user

def remove(db: Session, id: int):

    user = db.query(User).filter(User.id==id).delete()

    db.commit()

    return user
    
    