from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Добро пожаловать в приложение FastAPI Todo!"}

app.include_router(todo_router)
