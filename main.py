import os
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from app.api.models.tablas import Base
from app.api.endpoints.endpoints import rutas
from sqlalchemy import create_engine

# Obtener variables de entorno
MYSQLHOST = os.getenv("MYSQLHOST")
MYSQLPORT = os.getenv("MYSQLPORT")
MYSQLUSER = os.getenv("MYSQLUSER")
MYSQLPASSWORD = os.getenv("MYSQLPASSWORD")
MYSQLDATABASE = os.getenv("MYSQLDATABASE")

# Construir URL de conexión
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{MYSQLUSER}:{MYSQLPASSWORD}@{MYSQLHOST}:{MYSQLPORT}/{MYSQLDATABASE}"
)

# Crear el engine dinámicamente
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear tablas solo si no estás en producción
if os.getenv("ENV") != "production":
    Base.metadata.create_all(bind=engine)

# Inicializar app
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Ruta raíz
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

# Incluir rutas del API
app.include_router(rutas)

# Para correr localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
