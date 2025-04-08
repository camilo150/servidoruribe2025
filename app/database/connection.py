#Conexión con la base de datos

#Importación de las librerías

from sqlalchemy import create_engine,event #Llamar la librería para la comunicación con la base de datos
from sqlalchemy.orm import sessionmaker #abrir un canal hacia la base de datos
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv() #carga las variables de mi archivo env que son las variables de entorno

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)