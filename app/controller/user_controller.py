from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])
user_service = UserService()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user in the system.

    Args:
        user (UserCreate): The user data containing name, email, and phone_number.
        db (Session): Database session dependency.

    Returns:
        UserResponse: The newly created user record including their unique ID.
    """
    return user_service.create_user(db, user)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    """
    Retrieve a list of all active users.

    Note: This only returns users where 'deleted_at' is null (Soft Delete filter).

    Args:
        db (Session): Database session dependency.

    Returns:
        list[UserResponse]: A list of user records.
    """
    return user_service.list_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific user by their ID.

    Args:
        user_id (int): The unique identifier of the user.
        db (Session): Database session dependency.

    Returns:
        UserResponse: The requested user record if found.

    Raises:
        HTTPException: 404 error if the user does not exist or is soft-deleted.
    """
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    """
    Update an existing user's information.

    Args:
        user_id (int): The unique identifier of the user to update.
        user_data (UserUpdate): The updated fields (name, email, or phone).
        db (Session): Database session dependency.

    Returns:
        UserResponse: The updated user record.

    Raises:
        HTTPException: 404 error if the user does not exist.
    """
    user = user_service.update_user(db, user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Soft delete a user from the system.

    Sets the 'deleted_at' timestamp instead of removing the row from the database.

    Args:
        user_id (int): The unique identifier of the user to delete.
        db (Session): Database session dependency.

    Returns:
        None: Returns an empty body with status 204.

    Raises:
        HTTPException: 404 error if the user does not exist.
    """
    success = user_service.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return None