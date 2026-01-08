from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate
from datetime import datetime

class UserRepository:
    def get_all(self, db: Session):
        return db.query(User).filter(User.deleted_at == None).all()

    def get_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id, User.deleted_at == None).first()

    def create(self, db: Session, user: UserCreate):
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(self, db: Session, user_id: int, user_data: UserUpdate):
        db_user = self.get_by_id(db, user_id)
        if db_user:
            for key, value in user_data.model_dump(exclude_unset=True).items():
                setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
        return db_user

    def soft_delete(self, db: Session, user_id: int):
        db_user = self.get_by_id(db, user_id)
        if db_user:
            db_user.deleted_at = datetime.now()
            db.commit()
            return True
        return False