from pydantic import BaseModel


class Fruit(BaseModel):
    title: str
    description: str
    datetime: str
    entry_content: str = ""
    img_detail: str
    img: str
    img_detail_items: list = []