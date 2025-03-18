# Sin patrón State
class ReproductorMusica:
    def __init__(self):
        # Estado representado como una variable
        self.estado = "detenido"  # Estados posibles: detenido, reproduciendo, pausado
        self.cancion_actual = None
    
    def reproducir(self):
        if self.estado == "detenido":
            print("▶️ Iniciando reproducción")
            self.estado = "reproduciendo"
        elif self.estado == "pausado":
            print("▶️ Reanudando reproducción")
            self.estado = "reproduciendo"
        elif self.estado == "reproduciendo":
            print("⚠️ Ya está reproduciendo")
    
    def pausar(self):
        if self.estado == "reproduciendo":
            print("⏸️ Reproducción pausada")
            self.estado = "pausado"
        elif self.estado == "pausado":
            print("⚠️ Ya está pausado")
        elif self.estado == "detenido":
            print("⚠️ No se puede pausar, no hay reproducción activa")
    
    def detener(self):
        if self.estado == "reproduciendo" or self.estado == "pausado":
            print("⏹️ Reproducción detenida")
            self.estado = "detenido"
        elif self.estado == "detenido":
            print("⚠️ Ya está detenido")
    
    def siguiente(self):
        if self.estado == "reproduciendo" or self.estado == "pausado":
            print("⏭️ Pasando a la siguiente canción")
        else:
            print("⚠️ No hay reproducción activa")
    
    def anterior(self):
        if self.estado == "reproduciendo" or self.estado == "pausado":
            print("⏮️ Volviendo a la canción anterior")
        else:
            print("⚠️ No hay reproducción activa")

# Cliente
reproductor = ReproductorMusica()

# Secuencia de operaciones
reproductor.reproducir()  # Inicia reproducción
reproductor.siguiente()   # Pasa a siguiente canción
reproductor.pausar()      # Pausa
reproductor.pausar()      # Ya está pausado
reproductor.reproducir()  # Reanuda
reproductor.detener()     # Detiene
reproductor.anterior()    # No hay reproducción

# Problemas:
# - Código lleno de condicionales dependientes del estado
# - Difícil añadir nuevos estados o comportamientos
# - A medida que aumentan los estados, el código se vuelve más complejo
# - Las transiciones de estado están dispersas por todo el código