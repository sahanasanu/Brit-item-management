from fastapi import FastAPI
from app.routes import auth_routes, item_routes
from app.utils.database import client, db  # Import the MongoDB client and database

app = FastAPI()

# Use the startup event to initialize any necessary components
@app.on_event("startup")
async def on_startup():
    # Here you could perform actions like loading initial data or checking connectivity
    print("Application startup - MongoDB connected")

# Use the shutdown event to close the database connection if needed
@app.on_event("shutdown")
async def on_shutdown():
    # Optionally, close the MongoDB connection when the application shuts down
    client.close()
    print("Application shutdown - MongoDB connection closed")

# Include routes
app.include_router(auth_routes.router, prefix="/auth")
app.include_router(item_routes.router, prefix="/items")

@app.get("/")
def root():
    return {"message": "Welcome to the Item Management App"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
