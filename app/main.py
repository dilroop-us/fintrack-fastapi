from fastapi import FastAPI
from app.routers import users, categories

app = FastAPI(title="FinTrack API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Welcome to the FinTrack API"}

app.include_router(users.router)
app.include_router(categories.router)
