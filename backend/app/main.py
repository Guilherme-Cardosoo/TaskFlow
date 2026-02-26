from fastapi import FastAPI
from .routers import tasks

app = FastAPI(title="TaskFlow API")

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "TaskFlow API is running 🚀"}