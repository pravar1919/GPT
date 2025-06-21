from pydantic import BaseModel


class DataInput(BaseModel):
    pass


class Output(BaseModel):
    description: str
    score: float
