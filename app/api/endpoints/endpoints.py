from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.DTO.dtos import ProveedorDTO, ProvedorDTOEnvio, LogisticaDTO, LogisticaDTOEnvio
from app.api.models.tablas import Proveedor, Logistica
from app.database.connection import SessionLocal, engine

rutas = APIRouter()

# Rutina para conectarse a la base de datos
def conectarConBD():
    try:
        baseDatos=SessionLocal()
        yield baseDatos
        
    except Exception as error:
        baseDatos.rollback()
        raise error
    
    finally:
        baseDatos.close()  
    
# Ruta para consultar  ---------------------------------------------------------------------------------------


@rutas.get("/consultarProveedores", response_model=List[ProvedorDTOEnvio], summary="servicio para consultar los proveedores")
def buscarProveedores(database:Session=Depends(conectarConBD)):
    try:
        proveedores=database.query(Proveedor).all()
        return [ProvedorDTOEnvio(**proveedor.__dict__) for proveedor in proveedores]

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=404, detail=f"Tenemos un error: {error}")
    

@rutas.get("/consultarLogisticas", response_model=List[LogisticaDTOEnvio], summary="servicio para consultar la logística")
def buscarLogistica(database:Session=Depends(conectarConBD)):
    try:
        logisticas=database.query(Logistica).all()
        return [LogisticaDTOEnvio(**logistica.__dict__) for logistica in logisticas]
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=404, detail=f"Tenemos un error: {error}")    
    

# Ruta para guardar ---------------------------------------------------------------------------------------------------------
@rutas.post("/proveedor",response_model=ProvedorDTOEnvio,summary="servicio para guardar un proveedor en la base de datos")
def guardarProveedor(datosProveedor:ProveedorDTO,database:Session=Depends(conectarConBD)):
    try:
        proveedorAGuardar = Proveedor(
            nombres=datosProveedor.nombres,
            documento=datosProveedor.documento,
            direccion=datosProveedor.direccion,
            ciudad=datosProveedor.ciudad,
            representante=datosProveedor.representante,
            telefonoContacto=datosProveedor.telefonoContacto,
            correo=datosProveedor.correo,
            fechaDeEnvio=datosProveedor.fechaDeEnvio,
            costoDeEnvio=datosProveedor.costoDeEnvio,
            descripcion=datosProveedor.descripcion
        )
        database.add(proveedorAGuardar)
        database.commit()
        database.refresh(proveedorAGuardar)
        respuestaProvedor =ProvedorDTOEnvio(**proveedorAGuardar.__dict__)
        return respuestaProvedor
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un error: {error}")
    
@rutas.post("/logistica", response_model=LogisticaDTOEnvio, summary="servicio para guardar logística en la base de datos")
def guardarLogistica(datosLogistica: LogisticaDTO,database:Session=Depends(conectarConBD)):
    try:
        logisticaAGuardar = Logistica(
            nombreEncargado=datosLogistica.nombreEncargado,
            correoEncargado=datosLogistica.correoEncargado,
            contactoEncargado=datosLogistica.contactoEncargado,
            fechaEnvio=datosLogistica.fechaEnvio,
            descripcion=datosLogistica.descripcion
        )
        database.add(logisticaAGuardar)
        database.commit()
        database.refresh(logisticaAGuardar)
        respuestaLogistica = LogisticaDTOEnvio(**logisticaAGuardar.__dict__)
        return respuestaLogistica
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=404, detail=f"Tenemos un error: {error}")

    