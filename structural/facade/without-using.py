# Sin patrón Facade
class Amplificador:
    def encender(self):
        return "Amplificador encendido"
    
    def apagar(self):
        return "Amplificador apagado"
    
    def configurar_volumen(self, nivel):
        return f"Volumen configurado a {nivel}"
    
    def configurar_fuente(self, fuente):
        return f"Fuente configurada: {fuente}"

class ReproductorDVD:
    def encender(self):
        return "Reproductor DVD encendido"
    
    def apagar(self):
        return "Reproductor DVD apagado"
    
    def reproducir(self, pelicula):
        return f"Reproduciendo '{pelicula}'"
    
    def detener(self):
        return "Reproducción detenida"
    
    def expulsar(self):
        return "DVD expulsado"

class Proyector:
    def encender(self):
        return "Proyector encendido"
    
    def apagar(self):
        return "Proyector apagado"
    
    def modo_pantalla_ancha(self):
        return "Proyector en modo pantalla ancha (16:9)"

class LucesTeatrales:
    def atenuar(self, nivel):
        return f"Luces atenuadas al {nivel}%"
    
    def encender(self):
        return "Luces encendidas"

class PantallaDeCine:
    def bajar(self):
        return "Pantalla bajada"
    
    def subir(self):
        return "Pantalla subida"

# Cliente
# Para ver una película, el cliente debe interactuar con cada componente
def ver_pelicula(pelicula):
    # Inicializar todos los componentes
    amplificador = Amplificador()
    dvd = ReproductorDVD()
    proyector = Proyector()
    luces = LucesTeatrales()
    pantalla = PantallaDeCine()
    
    # Secuencia compleja de operaciones
    print(pantalla.bajar())
    print(proyector.encender())
    print(amplificador.encender())
    print(amplificador.configurar_fuente("DVD"))
    print(amplificador.configurar_volumen(8))
    print(luces.atenuar(30))
    print(dvd.encender())
    print(dvd.reproducir(pelicula))
    
    # Muchos pasos para una operación común

# Y para terminar, otra secuencia compleja
def terminar_pelicula():
    amplificador = Amplificador()
    dvd = ReproductorDVD()
    proyector = Proyector()
    luces = LucesTeatrales()
    pantalla = PantallaDeCine()
    
    print(dvd.detener())
    print(dvd.expulsar())
    print(dvd.apagar())
    print(amplificador.apagar())
    print(proyector.apagar())
    print(luces.encender())
    print(pantalla.subir())

# Cliente tiene que conocer muchos detalles
ver_pelicula("El Padrino")
print("\nTerminando la película:")
terminar_pelicula()