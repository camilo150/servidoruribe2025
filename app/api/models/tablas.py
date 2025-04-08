from sqlalchemy import Column,String,Integer,Date
 #todas las tablas en el mismo archivo, se puede en otros pero para pragmarismo no
from app.database.connection import Base
#llamado a la base para crear tablas


#definir modelos d ela base de datos

class Proveedor (Base) :
    __tablename__ = 'proveedores'
    
    id = Column(Integer, primary_key=True, autoincrement=True) # llave primaria y autoincrementa
    nombres=Column(String(50))
    documento=Column(String(50))
    direccion=Column(String(50))
    ciudad=Column(String(50))
    representante=Column(String(50))
    telefonoContacto=Column(String(50))
    correo=Column(String(50))
    fechaDeEnvio=Column(Date)
    costoDeEnvio=Column(Integer)
    descripcion=Column(String(50))

class Logistica (Base):
    __tablename__ = 'logistica'  #

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreEncargado = Column(String(50))
    correoEncargado = Column(String(50))  
    contactoEncargado = Column(String(50))  
    fechaEnvio = Column(Date)
    descripcion = Column(String(50))