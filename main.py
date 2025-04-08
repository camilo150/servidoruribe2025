import os
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from app.api.models.tablas import Base
from app.api.endpoints.endpoints import rutas
from app.database.connection import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)