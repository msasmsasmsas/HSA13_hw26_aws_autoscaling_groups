# Import FastAPI
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI in Docker on AWS!"}

# Note: FastAPI is async by default, making it suitable for high-performance applications
