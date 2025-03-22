from sqlalchemy import Column,String,Integer,Date
from sqlalchemy.ext.declarative import declarative_base #todas las tablas en el mismo archivo, se puede en otros pero para pragmarismo no

#llamado a la base para crear tablas
Base = declarative_base()

#definir modelos d ela base de datos

class Proveedor (Base) :
    
    __tablename__='proveedores'
    id = Column(Integer, primary_key=True, autoincrement=True) # llave primaria y autoincrementa
    nombres=Column(String(50))
    documento=Column(String(50))
    Direccion=Column(String(50))
    Ciudad=Column(String(50))
    Representante=Column(String(50))
    telefonoContacto=Column(String(50))
    Correo=Column(String(50))
    fechaDeEnvio=Column(Date)
    costoDeEnvio=Column(Integer)
    Descripcion=Column(String(50))



class Logistica:
    __tablename__ = 'logistica'  #

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreEncargado = Column(String(50))
    correoEncargado = Column(String(50))  
    contactoEncargado = Column(String(50))  
    fechaEnvio = Column(Date)
    Descripcion = Column(String(50))