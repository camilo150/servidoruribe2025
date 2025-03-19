from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends


from app.api.DTO.dtos import ProovedorDTOEnvio,ProveedorDTO,LogisticaDTO,LogisticaDTOEnvio
from app.api.models.tablas import Proveedor,Logistica
from app.database.connection import SessionLocal,engine

rutas = APIRouter()

#rutina para conectarnos a la base de datos

def ConectarConBd():
    try:
        baseDeDatos = SessionLocal()
        yield baseDeDatos

    except Exception as error:
        baseDeDatos.rollback
        raise error
    
    finally: 
        baseDeDatos.close()

#rutina para construir servicios web

@rutas.post("/proveedor",response_model=ProovedorDTOEnvio,summary="servicio para guardar un proveedor en la BD")

def guardarProveedor(datosProveedor:ProveedorDTO,database:Session=Depends(ConectarConBd)):
        try:
            provedorAguar=Proveedor(
            nombres=datosProveedor.nombres,
            documento=datosProveedor.documento,
            Direccion=datosProveedor.Direccion,
            Ciudad=datosProveedor.Ciudad,
            Representante= datosProveedor.Representante,
            telefonoContacto=datosProveedor.telefonoContacto,
            Correo=datosProveedor.Correo,
            fechaDeEnvio=datosProveedor.fechaDeEnvio,
            costoDeEnvio=datosProveedor.costoDeEnvio,
            Descripcion= datosProveedor.Descripcion
            )
            database.add(provedorAguar)
            database.commit()
            database.refresh(provedorAguar)
            return provedorAguar

        except Exception as error:
            database.rollback()
            raise HTTPException(status_code=400,detail=f"tenemos un error {error}")
            

@rutas.post("/logistica",response_model=LogisticaDTOEnvio,summary="servicio para guardar logistica en la BD")
def guardarLogistica(datosLogistica:LogisticaDTO,database:Session=Depends(ConectarConBd)):
    try:
        logisticaAguardar=Logistica(
            nombreEncargado=datosLogistica.nombreEncargado,
            correoEncargado=datosLogistica.correoEncargado,
            contactoEncargado=datosLogistica.contactoEncargado,
            fechaEnvio=datosLogistica.fechaEnvio,
            Descripcion=datosLogistica.Descripcion
        )   
        database.add()
        database.commit()
        database.refresh(logisticaAguardar)
        return logisticaAguardar 
    except Exception as error: 
        database.rollback()
        raise HTTPException(status_code=400,detail=f"tenemos un error {error}") 
    
    #rutina para consultar los proveedores
@rutas.get("/proveedor",response_model=[ProovedorDTOEnvio],summary="servicio para traer todos los provedores")
def buscarProveedor(database:Session=Depends(ConectarConBd)):
    try:
        Proveedores = database.query(Proveedor).all
        return Proveedores

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400,detail=f"tenemos un error {error}")
    

@rutas.get("/logistica",response_model=[LogisticaDTOEnvio],summary="servicio para traer todos la logistica")
def buscarLogistica(database:Session=Depends(ConectarConBd)):
    try:
        Logisticas = database.query(Logistica).all
        return Logisticas

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400,detail=f"tenemos un error {error}") 