from typing import Union
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "sajankumar": {
        "username": "sajankumar",
        "full_name": "Sajan Kumar",
        "email": "sajan@test.com",
        "hashed_password": "fakehashedpassword",
        "disabled": True,
    },
}

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

class UserInDB(User):
    hashed_password: str

def fake_hash_password(password: str):
    return "fakehashed" + password

