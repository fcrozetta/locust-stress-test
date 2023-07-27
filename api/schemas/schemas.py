import uuid
from pydantic import BaseModel, Field


class SuccessResponse(BaseModel):
    operation_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    message: str = "Success"


class InputModel(BaseModel):
    name: str
    age: int
