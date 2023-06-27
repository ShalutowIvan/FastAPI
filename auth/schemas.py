#схемы для создания пользователя, редактирования пользователя
# import uuid

from fastapi_users import schemas


# class UserRead(schemas.BaseUser[uuid.UUID]):
#     pass
#тут наследуется функционал и классы работают как наследники, их можно дописывать
class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str    
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        orm_mode = True



class UserCreate(schemas.BaseUserCreate):#тут допишем немного. Далее роутеры для аутха. Их добавляем в main.py
    username: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


# class UserUpdate(schemas.BaseUserUpdate):
#     pass