from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Proveedor(Base):
    __tablename__ = 'proveedores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(50))
    documento = Column(String(50))
    direccion = Column(String(50))
    ciudad = Column(String(50))
    representante = Column(String(50))
    telefonoContacto = Column(String(50))
    correo = Column(String(50))
    fechaDeEnvio = Column(Date)
    costoDeEnvio = Column(Integer)
    descripcion = Column(String(50))

class Logistica(Base):
    __tablename__ = 'logistica'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreEncargado = Column(String(50))
    correoEncargado = Column(String(50))
    contactoEncargado = Column(String(50))
    fechaEnvio = Column(Date)
    descripcion = Column(String(50))