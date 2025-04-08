#objetos de transferencia de datos = DTO filtro
from pydantic import BaseModel,Field
from datetime import date

class ProveedorDTO(BaseModel) : #DTO de recepcion
    nombres:str
    documento:str
    direccion:str
    ciudad:str
    representante:str
    telefonoContacto:str
    correo:str
    fechaDeEnvio:date
    costoDeEnvio:int
    descripcion:str   #todos esos son los parametros a recibir si no está aqui no se recibe
    class Config:
        orm_mode = True

class ProvedorDTOEnvio(BaseModel): #DTO de respuesta
    id:int
    nombres:str
    documento:str
    direccion:str
    ciudad:str
    representante:str
    telefonoContacto:str
    correo:str
    fechaDeEnvio:date
    costoDeEnvio:int
    descripcion:str 
    class Config:
        orm_mode = True

class LogisticaDTO(BaseModel):
    nombreEncargado:str
    correoEncargado:str  
    contactoEncargado:str
    fechaEnvio:date 
    descripcion:str
    class Config:
        orm_mode = True

class LogisticaDTOEnvio(BaseModel):
    id:int
    nombreEncargado:str
    correoEncargado:str  
    contactoEncargado:str
    fechaEnvio:date 
    descripcion:str
    class Config:
        orm_mode = True