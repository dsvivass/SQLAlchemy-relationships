from src.declarative_base import Base
from sqlalchemy import create_engine, Column, Integer, String, Enum 
from sqlalchemy.orm import relationship

import enum

class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3

class Album(Base):
    __tablename__ = 'album'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    ano = Column(Integer)
    descripcion = Column(String)
    medio = Column(Enum(Medio))
    
    # canciones = relationship('Cancion', cascade='all, delete, delete-orphan', back_populates="album")
    canciones = relationship('Cancion', secondary='album_cancion', back_populates="albumes")
    # cascade allows to delete all the songs of the album when the album is deleted
    # back_populates allows to have a reference to the songs of the album