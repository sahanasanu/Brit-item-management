from pymongo.collection import Collection
from app.schemas import ItemCreate

async def create_item(item: ItemCreate, user_id: int, collection: Collection) -> dict:
    """
    Create a new item and store it in the collection.
    """
    db_item = {
        "name": item.name,
        "price": item.price,
        "owner_id": user_id
    }
    result = await collection.insert_one(db_item)
    db_item["_id"] = result.inserted_id
    return db_item

def get_items_for_user(user_id: int, collection: Collection) -> list:
    """
    Retrieve all items for the specified user.
    """
    items_cursor = collection.find({"owner_id": user_id})
    items = list(items_cursor)  # Convert cursor to list synchronously
    return items
