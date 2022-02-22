from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.declarative_base import Base

class Interprete(Base):
    __tablename__ = 'interprete'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    texto_curiosidades = Column(String)
    
    cancion_id = Column(Integer, ForeignKey('cancion.id'))
    cancion = relationship('Cancion', back_populates='interpretes')