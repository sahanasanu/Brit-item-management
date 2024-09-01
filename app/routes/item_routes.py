from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request
from starlette.responses import JSONResponse

from app.schemas import ItemCreate, ItemResponse
from app.services.item_service import create_item, get_items_for_user
from app.utils.token import verify_token, get_current_user
from sqlalchemy.orm import Session
from app.utils.database import get_db
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Initialize the templates object
templates = Jinja2Templates(directory="app/templates")

@router.post("/add_items", response_model=ItemResponse)
def add_item(item: ItemCreate, current_user: int = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Add an item for the logged-in user.
    """
    try:
        return create_item(item, current_user, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list_items", response_model=List[ItemResponse])
def get_user_items(request: Request, current_user: int = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Get all items for the logged-in user and render the add_items template.
    """
    try:
        items = get_items_for_user(current_user, db)
        return templates.TemplateResponse("add_items.html", {"request": request, "items": items})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/summary")
async def get_summary(current_user: int = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Get the summary of all items and calculate the total price.
    """
    try:
        items = get_items_for_user(current_user, db)
        total_price = sum(float(item.price) for item in items)  # Convert Decimal to float
        item_list = [{"name": item.name, "price": float(item.price)} for item in items]  # Convert Decimal to float
        return JSONResponse(content={"total_price": total_price, "items": item_list})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))