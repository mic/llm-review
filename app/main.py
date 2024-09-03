from fastapi import FastAPI
from .routes import router
from .config import PORT

app = FastAPI()

# Include the routes from the routes module
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    print(f"Starting server on port: {PORT}")
    uvicorn.run(app, host="127.0.0.1", port=PORT)