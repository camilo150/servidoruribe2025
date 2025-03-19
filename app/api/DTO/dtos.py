#objetos de transferencia de datos = DTO filtro
from pydantic import BaseModel,Field
from datetime import date

class ProveedorDTO(BaseModel) : #DTO de recepcion
    nombres:str
    documento:str
    Direccion:str
    Ciudad:str
    Representante:str
    telefonoContacto:str
    Correo:str
    fechaDeEnvio:date
    costoDeEnvio:int
    Descripcion:str   #todos esos son los parametros a recibir si no está aqui no se recibe

class ProovedorDTOEnvio(BaseModel): #DTO de respuesta
    id:int
    nombres:str
    documento:str
    Direccion:str
    Ciudad:str
    Representante:str
    telefonoContacto:str
    Correo:str
    fechaDeEnvio:date
    costoDeEnvio:int
    Descripcion:str

class LogisticaDTO(BaseModel):
    nombreEncargado:str
    correoEncargado:str  
    contactoEncargado:str
    fechaEnvio:str 
    Descripcion:str

class LogisticaDTOEnvio(BaseModel):
    id:int
    nombreEncargado:str
    correoEncargado:str  
    contactoEncargado:str
    fechaEnvio:str 
    Descripcion:str