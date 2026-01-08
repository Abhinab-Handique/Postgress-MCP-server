from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def list_users(self, db: Session):
        return self.repo.get_all(db)

    def get_user(self, db: Session, user_id: int):
        return self.repo.get_by_id(db, user_id)

    def create_user(self, db: Session, user_data: UserCreate):
        return self.repo.create(db, user_data)

    def update_user(self, db: Session, user_id: int, user_data: UserUpdate):
        return self.repo.update(db, user_id, user_data)

    def delete_user(self, db: Session, user_id: int):
        return self.repo.soft_delete(db, user_id)