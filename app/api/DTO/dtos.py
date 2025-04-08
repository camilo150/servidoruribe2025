from pydantic import BaseModel
from datetime import date

class ProveedorDTO(BaseModel):
    nombres: str
    documento: str
    direccion: str
    ciudad: str
    representante: str
    telefonoContacto: str
    correo: str
    fechaDeEnvio: date
    costoDeEnvio: int
    descripcion: str
    class Config:
        orm_mode = True

class ProvedorDTOEnvio(ProveedorDTO):
    id: int

class LogisticaDTO(BaseModel):
    nombreEncargado: str
    correoEncargado: str
    contactoEncargado: str
    fechaEnvio: date
    descripcion: str
    class Config:
        orm_mode = True

class LogisticaDTOEnvio(LogisticaDTO):
    id: int