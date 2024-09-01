from fastapi import APIRouter, HTTPException, Depends, Request, Response
from starlette.responses import JSONResponse
from app.schemas import UserCreate, UserResponse, UserLogin
from app.services.auth_service import create_user, authenticate_user
from app.utils.token import verify_token, create_access_token
from fastapi.templating import Jinja2Templates
from app.utils.database import get_db

router = APIRouter()

# Initialize the templates object
templates = Jinja2Templates(directory="app/templates")

@router.get("/create_account")
async def show_create_account_page(request: Request):
    """
    Render the Create Account page.
    """
    return templates.TemplateResponse("create_account.html", {"request": request})

@router.post("/create_new_account", response_model=UserResponse)
async def create_new_account(user_data: UserCreate, db=Depends(get_db)):
    """
    Create a new user account using JSON input.
    """
    existing_user = await authenticate_user(user_data.username, user_data.password, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    try:
        # If user does not exist, create a new user
        return await create_user(user_data, collection)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")

@router.get("/login")
async def show_login_page(request: Request):
    """
    Render the Login page.
    """
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(user_data: UserLogin, response: Response, collection=Depends(get_collection)):
    user = await authenticate_user(user_data.username, user_data.password, collection)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(user["_id"])
    response.set_cookie(key="token", value=access_token, httponly=True)  # Set the token as an HTTP-only cookie
    return {"message": "Login successful"}

@router.post("/logout")
async def logout(response: Response):
    """
    Perform logout by invalidating the JWT token.
    This could involve blacklisting the token in a real-world scenario.
    """
    # Invalidate the token or perform other logout operations here
    # For now, just respond with success
    response = JSONResponse(content={"detail": "Logged out successfully"})
    response.delete_cookie(key="token")  # This will delete the cookie if you are using cookies
    return response
