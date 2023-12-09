from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str
    
class SignsRequest(BaseModel):
    signs: list
    l: int = 10