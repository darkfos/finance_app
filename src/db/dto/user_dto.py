from typing import Annotated
from pydantic import BaseModel, Field, EmailStr
from bson.objectid import ObjectId


class AddNewUser(BaseModel):

    email: Annotated[str, Field(min_length=6, max_length=80)]
    password: Annotated[str, Field(min_length=6)]


class UpdateUserInformation(BaseModel):

    id: Annotated[ObjectId, Field()]
    user_name: Annotated[str, Field(min_length=1, max_length=120)]