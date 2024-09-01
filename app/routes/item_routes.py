from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request
from starlette.responses import JSONResponse
from app.schemas import ItemCreate, ItemResponse
from app.services.item_service import create_item, get_items_for_user
from app.utils.token import get_current_user
from app.utils.database import get_collection
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Initialize the templates object
templates = Jinja2Templates(directory="app/templates")

@router.post("/add_items", response_model=ItemResponse)
async def add_item(item: ItemCreate, current_user: str = Depends(get_current_user), collection=Depends(get_collection)):
    """
    Add an item for the logged-in user.
    """
    try:
        return await create_item(item, current_user, collection)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list_items", response_model=List[ItemResponse])
async def get_user_items(request: Request, current_user: str = Depends(get_current_user), collection=Depends(get_collection)):
    """
    Get all items for the logged-in user and render the add_items template.
    """
    try:
        items = await get_items_for_user(current_user, collection)
        return templates.TemplateResponse("add_items.html", {"request": request, "items": items})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/summary")
async def get_summary(request: Request, current_user: str = Depends(get_current_user), collection=Depends(get_collection)):
    """
    Get the summary of all items and calculate the total price.
    """
    try:
        items = await get_items_for_user(current_user, collection)
        total_price = sum(item["price"] for item in items)  # Adjusted for MongoDB documents
        return templates.TemplateResponse("summary.html", {
            "request": request,
            "total_price": total_price,
            "items": items
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
