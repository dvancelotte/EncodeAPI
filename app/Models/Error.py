from pydantic import BaseModel

class Erro(BaseModel):
    message: str
    