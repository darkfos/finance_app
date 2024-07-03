#System
from typing import Annotated


#Other libraries
from datetime import datetime
from pydantic import BaseModel, Field
from bson.objectid import ObjectId


class AddHistory(BaseModel):

    user_id: Annotated[ObjectId, Field()]
    from_operation: Annotated[str, Field(default="USD")]
    to_operation: Annotated[str, Field(default="USD")]
    date_operation: Annotated[datetime, Field(default=datetime.now())] = datetime.now()

    class Config:
        arbitrary_types_allowed = True