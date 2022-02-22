from src.declarative_base import Base, session, engine
from src.album import Album, Medio
from src.cancion import Cancion
from src.interprete import Interprete
from src.associationAlbumCancion import AlbumCancion

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    album1 = Album(titulo = 'test2', ano = 1996, descripcion = 'Mi descripcion', medio = Medio.DISCO)

    session.add(album1)
    session.commit()
    
    session.refresh(album1) # Refresh and get the current elemnt commited
    print(album1.id) # print the id of the album just commited
    
    cancion1 = Cancion(titulo = 'cancion1', minutos = 2, segundos = 34, compositor = 'Daniel')
    cancion2 = Cancion(titulo = 'cancion2', minutos = 3, segundos = 34, compositor = 'Daniel S')
    session.add(cancion1)
    session.add(cancion2)
    
    album1.canciones = [cancion1, cancion2]
    
    session.commit()
    
    session.refresh(album1)
    
    print(album1.canciones, album1.canciones[0].titulo, album1.canciones[1].titulo, album1.canciones[0].albumes)
    
    # print(cancion1.id, cancion1.album.id, cancion1.album.titulo, cancion1.album.ano, cancion1.album.descripcion, cancion1.album.medio, cancion1.album.canciones)
    
    
    # interprete1 = Interprete(nombre = 'test2', texto_curiosidades = 'Mi descripcion', cancion_id = 1)
    
    # session.add(interprete1)
    # session.commit()
    
    # singerToDelete = session\
    #     .query(Interprete)\
    #     .filter(Interprete.id == 1)\
    #     .first()
        
    # session.delete(singerToDelete)
    # session.commit()
    
    # songToDelete = session\
    #     .query(Cancion)\
    #     .filter(Cancion.id == 1)\
    #     .first()
        
    # session.delete(songToDelete)
    # session.commit()
    
    # albumToDelete = session\
    #     .query(Album)\
    #     .filter(Album.id == 1)\
    #     .first()
        
    # session.delete(albumToDelete)
    # session.commit()
    pass