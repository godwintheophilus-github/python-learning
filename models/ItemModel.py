from pydantic import BaseModel, Field


class Item(BaseModel):
    item_id: int
    item_name: str = Field("ABC",max_length=50,min_length=2)
