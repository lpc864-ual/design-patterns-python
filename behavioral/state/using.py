# Con patrón State
from abc import ABC, abstractmethod

# Estado (interfaz)
class EstadoReproductor(ABC):
    @abstractmethod
    def reproducir(self, reproductor):
        pass
    
    @abstractmethod
    def pausar(self, reproductor):
        pass
    
    @abstractmethod
    def detener(self, reproductor):
        pass
    
    @abstractmethod
    def siguiente(self, reproductor):
        pass
    
    @abstractmethod
    def anterior(self, reproductor):
        pass

# Estados concretos
class EstadoDetenido(EstadoReproductor):
    def reproducir(self, reproductor):
        print("▶️ Iniciando reproducción")
        reproductor.cambiar_estado(EstadoReproduciendo())
    
    def pausar(self, reproductor):
        print("⚠️ No se puede pausar, no hay reproducción activa")
    
    def detener(self, reproductor):
        print("⚠️ Ya está detenido")
    
    def siguiente(self, reproductor):
        print("⚠️ No hay reproducción activa")
    
    def anterior(self, reproductor):
        print("⚠️ No hay reproducción activa")

class EstadoReproduciendo(EstadoReproductor):
    def reproducir(self, reproductor):
        print("⚠️ Ya está reproduciendo")
    
    def pausar(self, reproductor):
        print("⏸️ Reproducción pausada")
        reproductor.cambiar_estado(EstadoPausado())
    
    def detener(self, reproductor):
        print("⏹️ Reproducción detenida")
        reproductor.cambiar_estado(EstadoDetenido())
    
    def siguiente(self, reproductor):
        print("⏭️ Pasando a la siguiente canción")
    
    def anterior(self, reproductor):
        print("⏮️ Volviendo a la canción anterior")

class EstadoPausado(EstadoReproductor):
    def reproducir(self, reproductor):
        print("▶️ Reanudando reproducción")
        reproductor.cambiar_estado(EstadoReproduciendo())
    
    def pausar(self, reproductor):
        print("⚠️ Ya está pausado")
    
    def detener(self, reproductor):
        print("⏹️ Reproducción detenida")
        reproductor.cambiar_estado(EstadoDetenido())
    
    def siguiente(self, reproductor):
        print("⏭️ Pasando a la siguiente canción")
        reproductor.cambiar_estado(EstadoReproduciendo())
    
    def anterior(self, reproductor):
        print("⏮️ Volviendo a la canción anterior")
        reproductor.cambiar_estado(EstadoReproduciendo())

# Contexto
class ReproductorMusica:
    def __init__(self):
        # Estado inicial
        self.estado = EstadoDetenido()
        self.cancion_actual = None
    
    def cambiar_estado(self, estado):
        self.estado = estado
    
    # Estos métodos delegan al estado actual
    def reproducir(self):
        self.estado.reproducir(self)
    
    def pausar(self):
        self.estado.pausar(self)
    
    def detener(self):
        self.estado.detener(self)
    
    def siguiente(self):
        self.estado.siguiente(self)
    
    def anterior(self):
        self.estado.anterior(self)

# Cliente
reproductor = ReproductorMusica()

# La misma secuencia de operaciones que antes
reproductor.reproducir()  # Inicia reproducción
reproductor.siguiente()   # Pasa a siguiente canción
reproductor.pausar()      # Pausa
reproductor.pausar()      # Ya está pausado
reproductor.reproducir()  # Reanuda
reproductor.detener()     # Detiene
reproductor.anterior()    # No hay reproducción

# Añadir un nuevo estado es sencillo
class EstadoSilenciado(EstadoReproductor):
    def reproducir(self, reproductor):
        print("▶️ Reproduciendo (sin sonido)")
        reproductor.cambiar_estado(EstadoReproduciendo())
    
    def pausar(self, reproductor):
        print("⏸️ Pausado (sin sonido)")
        reproductor.cambiar_estado(EstadoPausado())
    
    def detener(self, reproductor):
        print("⏹️ Reproducción detenida")
        reproductor.cambiar_estado(EstadoDetenido())
    
    def siguiente(self, reproductor):
        print("⏭️ Siguiente canción (sin sonido)")
    
    def anterior(self, reproductor):
        print("⏮️ Canción anterior (sin sonido)")

# Ventajas:
# - Cada estado se encapsula en su propia clase
# - Las transiciones están claramente definidas
# - Fácil añadir nuevos estados sin modificar estados existentes
# - El código es más limpio y mantenible
# - El polimorfismo reemplaza a las condicionales