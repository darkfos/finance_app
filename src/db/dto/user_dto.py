#System
from typing import Annotated

#Other libraries
import pydantic.dataclasses
from pydantic import BaseModel, Field, EmailStr
from bson.objectid import ObjectId


class AddNewUser(BaseModel):

    email: Annotated[EmailStr, Field(min_length=6, max_length=80)]
    password: Annotated[str, Field(min_length=6)]

    class Config:
        arbitrary_types_allowed = True


class UpdateUserInformation(BaseModel):

    id: Annotated[ObjectId, Field()]
    user_name: Annotated[str, Field(min_length=1, max_length=120)]

    class Config:
        arbitrary_types_allowed = True