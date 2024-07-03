#System
import datetime
from typing import Annotated
from random import choice

#Other libraries
import pydantic.dataclasses
from pydantic import BaseModel, Field, EmailStr
from bson.objectid import ObjectId


class AddNewUser(BaseModel):

    email: Annotated[EmailStr, Field(min_length=6, max_length=80)]
    password: Annotated[str, Field(min_length=6)]
    data_registration: Annotated[datetime.datetime, Field(default=datetime.datetime.now())] = datetime.datetime.now()
    data_update: Annotated[datetime.datetime, Field(default=datetime.datetime.now())] = datetime.datetime.now()
    username: Annotated[str, Field(max_length=50)] = choice(("Crisp222", "Meow234r5", "Eduard", "Tark99", "User", "Not22"))
    count_general_convert: Annotated[int, Field(default=0)] = 0
    count_convert_coin: Annotated[int, Field(default=0)] = 0
    count_convert_value: Annotated[int, Field(default=0)] = 0

    class Config:
        arbitrary_types_allowed = True


class UpdateUserCountValue(BaseModel):

    _id: Annotated[ObjectId, Field()]
    count_general_convert: Annotated[int, Field(default=0)] = None
    count_convert_value: Annotated[int, Field(default=0)] = None

    class Config:
        arbitrary_types_allowed = True