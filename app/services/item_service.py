from pymongo.collection import Collection
from app.schemas import ItemCreate
from fastapi import Depends
from app.utils.database import get_collection

async def create_item(item: ItemCreate, user_id: int, collection: Collection = Depends(get_collection)) -> dict:
    db_item = {
        "name": item.name,
        "price": item.price,
        "owner_id": user_id
    }
    result = await collection.insert_one(db_item)
    db_item["_id"] = result.inserted_id
    return db_item

async def get_items_for_user(user_id: int, collection: Collection = Depends(get_collection)) -> list:
    items_cursor = collection.find({"owner_id": user_id})
    items = await items_cursor.to_list(length=100)  # Adjust length as needed
    return items
