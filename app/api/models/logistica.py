from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base  

Base = declarative_base()

class Logistica(Base):  
    __tablename__ = 'logistica'  

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreEncargado = Column(String(50))
    correoEncargado = Column(String(50))  
    contactoEncargado = Column(String(50))  
    fechaEnvio = Column(Date)
    Descripcion = Column(String(50))