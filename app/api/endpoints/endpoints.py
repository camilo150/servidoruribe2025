from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.DTO.dtos import ProveedorDTO, ProvedorDTOEnvio, LogisticaDTO, LogisticaDTOEnvio
from app.api.models.tablas import Proveedor, Logistica
from app.database.connection import SessionLocal

rutas = APIRouter()

def conectarConBD():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rutas.get("/consultarProveedores", response_model=List[ProvedorDTOEnvio])
def buscarProveedores(db: Session = Depends(conectarConBD)):
    proveedores = db.query(Proveedor).all()
    return proveedores

@rutas.get("/consultarLogisticas", response_model=List[LogisticaDTOEnvio])
def buscarLogistica(db: Session = Depends(conectarConBD)):
    logisticas = db.query(Logistica).all()
    return logisticas

@rutas.post("/proveedor", response_model=ProvedorDTOEnvio)
def guardarProveedor(datos: ProveedorDTO, db: Session = Depends(conectarConBD)):
    proveedor = Proveedor(**datos.dict())
    db.add(proveedor)
    db.commit()
    db.refresh(proveedor)
    return proveedor

@rutas.post("/logistica", response_model=LogisticaDTOEnvio)
def guardarLogistica(datos: LogisticaDTO, db: Session = Depends(conectarConBD)):
    logistica = Logistica(**datos.dict())
    db.add(logistica)
    db.commit()
    db.refresh(logistica)
    return logistica