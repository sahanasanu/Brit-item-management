from sqlalchemy.orm import Session
from app.models import Item
from app.schemas import ItemCreate
from app.utils.database import get_db
from fastapi import Depends

def create_item(item: ItemCreate, user_id: int, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, price=item.price, owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items_for_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(Item).filter(Item.owner_id == user_id).all()
