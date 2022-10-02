from fastapi import APIRouter
from shopping_cart.schemas.address import Address
from shopping_cart.schemas.user import UserSchema
from shopping_cart.cruds.user import create_address, create_user, get_all_users, get_user_by_email, update_password, find_address_by_email

router = APIRouter(tags=['User'], prefix='/user')

@router.post('')
async def post_user(user: UserSchema):
    message = await create_user(user)
    return message

@router.get('/email/')
async def get_user_email(email: str):
    user = await get_user_by_email(email)
    return user

@router.get('/all/')
async def get_all():
    users_list = await get_all_users()
    return users_list

@router.put("/update")
async def password_update(email: str, new_password: str):
    update = await update_password(email, new_password)
    return update

@router.post('/address')
async def create_address_user(user: UserSchema, address: Address):
    data = await create_address(user, address)
    return data

@router.get("/address")
async def get_address(email: str):
    user = await find_address_by_email(email)
    return user