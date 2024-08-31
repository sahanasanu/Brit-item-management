from fastapi import FastAPI
from app.routes import auth_routes, item_routes
from app.utils.database import create_db_and_tables
import uvicorn

app = FastAPI()

# Use the startup event to initialize the database
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include routes
app.include_router(auth_routes.router, prefix="/auth")
app.include_router(item_routes.router, prefix="/items")

@app.get("/")
def root():
    return {"message": "Welcome to the Item Management App"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)