# Con patrón Iterator
from abc import ABC, abstractmethod

# Iterador abstracto
class Iterador(ABC):
    @abstractmethod
    def tiene_siguiente(self):
        pass
    
    @abstractmethod
    def siguiente(self):
        pass

# Colección abstracta
class Coleccion(ABC):
    @abstractmethod
    def crear_iterador(self):
        pass

# Iterador concreto
class IteradorPlaylist(Iterador):
    def __init__(self, playlist):
        self.playlist = playlist
        self.indice = 0
    
    def tiene_siguiente(self):
        return self.indice < len(self.playlist.canciones)
    
    def siguiente(self):
        if self.tiene_siguiente():
            cancion = self.playlist.canciones[self.indice]
            self.indice += 1
            return cancion
        return None

# Iterador concreto para recorrer en orden inverso
class IteradorPlaylistInverso(Iterador):
    def __init__(self, playlist):
        self.playlist = playlist
        self.indice = len(playlist.canciones) - 1
    
    def tiene_siguiente(self):
        return self.indice >= 0
    
    def siguiente(self):
        if self.tiene_siguiente():
            cancion = self.playlist.canciones[self.indice]
            self.indice -= 1
            return cancion
        return None

# Colección concreta
class Playlist(Coleccion):
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
    
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
    
    def crear_iterador(self):
        return IteradorPlaylist(self)
    
    def crear_iterador_inverso(self):
        return IteradorPlaylistInverso(self)

# Cliente
mi_playlist = Playlist("Éxitos 2023")
mi_playlist.agregar_cancion("Canción 1")
mi_playlist.agregar_cancion("Canción 2")
mi_playlist.agregar_cancion("Canción 3")

# Usando el iterador en orden normal
print("Reproduciendo en orden normal:")
iterador = mi_playlist.crear_iterador()
while iterador.tiene_siguiente():
    print(f"Reproduciendo: {iterador.siguiente()}")

# Usando el iterador en orden inverso
print("\nReproduciendo en orden inverso:")
iterador_inverso = mi_playlist.crear_iterador_inverso()
while iterador_inverso.tiene_siguiente():
    print(f"Reproduciendo: {iterador_inverso.siguiente()}")

# Implementación alternativa usando el protocolo de iteración de Python
class PlaylistPython(Coleccion):
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
    
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
    
    # Implementa el protocolo de iteración de Python
    def __iter__(self):
        self.indice = 0
        return self
    
    def __next__(self):
        if self.indice < len(self.canciones):
            cancion = self.canciones[self.indice]
            self.indice += 1
            return cancion
        else:
            raise StopIteration
    
    def crear_iterador(self):
        return iter(self)

# Cliente con el protocolo de Python
print("\nUsando el protocolo de iteración de Python:")
mi_playlist_python = PlaylistPython("Favoritos")
mi_playlist_python.agregar_cancion("Canción A")
mi_playlist_python.agregar_cancion("Canción B")
mi_playlist_python.agregar_cancion("Canción C")

# Python maneja la iteración automáticamente
for cancion in mi_playlist_python:
    print(f"Reproduciendo: {cancion}")

# Ventajas:
# - Encapsula los detalles de implementación de la colección
# - Permite diferentes formas de recorrer la misma colección
# - Simplifica la interfaz de la colección
# - Múltiples iteradores pueden recorrer la misma colección simultáneamente