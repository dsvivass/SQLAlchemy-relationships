from src.declarative_base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Cancion(Base):
    __tablename__ = 'cancion'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)
    
    albumes = relationship('Album', secondary='album_cancion', back_populates="canciones")
    
    interpretes = relationship('Interprete', cascade='all, delete, delete-orphan', back_populates='cancion')