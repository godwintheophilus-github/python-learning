
from typing import Union, Annotated
from fastapi import APIRouter, Query
from fastapi.params import Depends

from models.ItemModel import Item
from enum import Enum
router = APIRouter()
from dbactions import CreateTable
class EnumValues(Enum):
    a = "a"
    b = "b"
    c = "c"

class dependencyValidation:
    def __init__(self):
        pass
    def __call__(self,item_id):
        print(str(item_id) + " checked")
        return str(item_id)+"_modified_item_id"

@router.post("/setItems")
async def store_items(item: Annotated[Union[Item,None], None] = None):
    print(item)
    return {"status": "success", "item": item}

@router.post("getItem")
async def get_item(itemId: Annotated[Union[int,None],1]):
    print(itemId)
    return ""

@router.post("/enumExample")
async def post_enum(enumValues: EnumValues):
    return enumValues

dependencyValidationObject = dependencyValidation()

@router.post("/modifyTheItemId")
async def dependencyMapping(modifiedItemId: Annotated[Union[str,None],Depends(dependencyValidationObject)]):
    return modifiedItemId

@router.post("/createTable")
async def create_table():
    return {
        "data": CreateTable.create_table()
    }