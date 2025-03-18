# Sin patrón Iterator
class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
    
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
    
    # Sin iterador, el cliente debe conocer la estructura interna
    def obtener_canciones(self):
        return self.canciones

# Cliente
mi_playlist = Playlist("Éxitos 2023")
mi_playlist.agregar_cancion("Canción 1")
mi_playlist.agregar_cancion("Canción 2")
mi_playlist.agregar_cancion("Canción 3")

# El cliente accede directamente a la estructura de datos interna
canciones = mi_playlist.obtener_canciones()
for cancion in canciones:
    print(f"Reproduciendo: {cancion}")

# Problemas:
# - El cliente depende de la estructura interna de la colección
# - Si cambia la implementación interna, todos los clientes deben actualizarse
# - Difícil proporcionar diferentes formas de recorrer la colección